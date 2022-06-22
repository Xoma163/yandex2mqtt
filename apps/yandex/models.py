import datetime
import logging

import requests
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .consts import Status
from .model_consts import *
from ..main.models import UUIDModel, ChoiceArrayField
from ..mqtt.models import MqttConfig

mqtt_logger = logging.getLogger("mqtt")
yandex_logger = logging.getLogger("yandex")


class Room(models.Model):
    name = models.CharField("Комната", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "комната"
        verbose_name_plural = "комнаты"


class YandexDialog(models.Model):
    name = models.CharField("Название", max_length=100)
    oauth_token = models.CharField("OAuth токен", max_length=40,
                                   help_text="https://yandex.ru/dev/dialogs/smart-home/doc/reference-alerts/resources-alerts.html#resources-alerts__oauth")
    skill_id = models.UUIDField("ID навыка в яндексе",
                                help_text="https://dialogs.yandex.ru/developer/skills/{skill_id}")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "яндекс диалог"
        verbose_name_plural = "яндекс диалоги"


class Device(UUIDModel, models.Model):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html
    """
    author = models.ForeignKey(get_user_model(), verbose_name="Автор", on_delete=models.CASCADE, related_name="devices")
    yd = models.ForeignKey(YandexDialog, verbose_name="Яндекс диалог (навык)", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=100, help_text="Название которое будет указано в Яндексе")
    type = models.CharField("Тип", choices=DeviceTypeChoices, max_length=50, help_text="https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, verbose_name="Комната", null=True, blank=True, help_text="Если указано, устройство само добавится в Яндексе в нужную комнату")
    description = models.TextField("Описание", max_length=100, blank=True)
    custom_data = models.JSONField(default=dict, verbose_name="Кастомные данные", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "устройство"
        verbose_name_plural = "устройства"

    # yandex things
    def get_for_device_list(self):
        data = {
            "id": str(self.pk),
            "name": self.name,
            "type": self.type,
        }
        if self.room:
            data['room'] = self.room.name
        if self.description:
            data['description'] = self.description
        if self.custom_data:
            data['custom_data'] = self.custom_data
        if self.capabilities:
            data['capabilities'] = [x.get_for_device_list() for x in self.capabilities.all()]
        if self.properties:
            data['properties'] = [x.get_for_device_list() for x in self.properties.all()]

        return data

    def get_for_state(self):
        data = {
            'id': str(self.pk),
            'capabilities': []
        }
        if self.capabilities:
            for capability in self.capabilities.all():
                data['capabilities'] += capability.state
        return data

    def get_for_switch_state(self, new_values):
        data = {
            'id': str(self.pk),
            'capabilities': []
        }
        if self.capabilities:
            for capability in self.capabilities.all():
                for value in new_values:
                    if value['type'] == capability.type:
                        data['capabilities'].append(capability.set_state(value['state']))
                        break
        return data


class BaseAbilityModel(models.Model):
    # Общее
    name = models.CharField("Название", max_length=100, blank=True)
    type = models.CharField("Тип устройства", max_length=100)
    device = models.ForeignKey(Device, verbose_name="Устройство", on_delete=models.CASCADE)
    parameters = models.JSONField("Параметры", default=dict, editable=False)
    retrievable = models.BooleanField("Включенное оповещение", default=True,
                                      help_text="Признак включенного оповещения об изменении состояния умения при помощи сервиса уведомлений")
    reportable = models.BooleanField("Доступен ли запрос состояния", default=True,
                                     help_text="Доступен ли для данного умения устройства запрос состояния")
    state = models.JSONField(default=list, help_text="Стейт", blank=True)

    # mqtt
    mqtt_config = models.ForeignKey(MqttConfig, verbose_name="Конфигурация MQTT", on_delete=models.SET_NULL, null=True)
    state_topic = models.CharField("Топик для состояния", max_length=100)
    state_topic_retriever = models.CharField("JsonPathRetriever топика для состояния", default="",
                                             help_text="https://pypi.org/project/jsonpath-ng/ Пример: $.Sensors.Temperature",
                                             max_length=100, blank=True)

    def get_for_device_list(self):
        return {
            'type': self.type,
            'retrievable': self.retrievable,
            'reportable': self.reportable,
            'parameters': self.parameters,
        }

    def update_yandex_state(self):
        url = f"https://dialogs.yandex.net/api/v1/skills/{self.device.yd.skill_id}/callback/state"
        headers = {
            "Authorization": f"OAuth {self.device.yd.oauth_token}",
            "Content-Type": "application/json"
        }
        properties_or_capabilities = [{"type": self.type, "state": state} for state in self.state]
        if isinstance(self, Property):
            field = "properties"
        elif isinstance(self, Capability):
            field = "capabilities"
        else:
            raise NotImplementedError()
        data = {
            "ts": datetime.datetime.now().timestamp(),
            "payload": {
                "user_id": str(self.device.author.pk),
                "devices": [
                    {
                        "id": str(self.device.pk),
                        field: properties_or_capabilities
                    }
                ]
            }
        }
        res = requests.post(url, json=data, headers=headers)
        if not res.ok:
            yandex_logger.error(
                f"Ошибка при отправке запроса на обновление состояния устройства Запрос - {res.json()}. Отправленные данные - {data}")
        else:
            yandex_logger.info(f"Способность \"{self}\" устройства \"{self.device}\" была успешно обновлена")
        return res

    class Meta:
        abstract = True


class Capability(BaseAbilityModel, models.Model):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/capability-types.html
    """
    # Общее
    type = models.CharField("Тип устройства", max_length=100, choices=CapabilityTypeChoices)
    device = models.ForeignKey(Device, verbose_name="Устройство", related_name="capabilities", on_delete=models.CASCADE)

    # mqtt
    command_topic = models.CharField("Топик для команд", max_length=100)

    # ColorSetting
    color_model = models.CharField("Цветовая модель", max_length=10, choices=ColorModelChoices, blank=True)
    temp_k_min = models.PositiveIntegerField("Минимальная температура света", null=True, blank=True)
    temp_k_max = models.PositiveIntegerField("Максимальная температура света", null=True, blank=True)

    # Mode
    mode_instance = models.CharField("Название функции для свойства", max_length=50, choices=ModeInstanceChoices,
                                     blank=True)
    modes = ChoiceArrayField(models.CharField("Режимы", max_length=50, choices=ModeChoices), blank=True)

    # OnOff
    split = models.BooleanField("split", blank=True,
                                help_text="За включение/выключение устройства у провайдера отвечают разные команды")

    # Range
    range_instance = models.CharField("Название функции для свойства", max_length=50, choices=RangeInstanceChoices,
                                      blank=True)
    unit = models.CharField("Единица измерения", max_length=50, choices=RangeUnitChoices, blank=True)
    random_access = models.BooleanField("Произвольные значения", blank=True,
                                        help_text="Если эта возможность выключена, пользователю будет доступно только последовательное изменение значений — в большую или меньшую сторону. Например, изменение громкости телевизора при работе через ИК пульт.")
    range_min = models.PositiveIntegerField("Минимальное значение", null=True, blank=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(100)])
    range_max = models.PositiveIntegerField("Максимальное значение", null=True, blank=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(100)])
    range_precision = models.PositiveIntegerField("Шаг", blank=True, null=True)
    # Toggle
    toggle_instance = models.CharField("Название функции для свойства", max_length=50, choices=ToggleInstanceChoices,
                                       blank=True)
    # VideoStream
    protocol = models.CharField("Протокол", max_length=50, choices=ProtocolChoices, blank=True)

    def save(self, **kwargs):
        constructor_map = {
            CapabilityType.COLOR_SETTING.value: self.init_color_settings,
            CapabilityType.MODE.value: self.init_mode,
            CapabilityType.ON_OFF.value: self.init_on_off,
            CapabilityType.RANGE.value: self.init_range,
            CapabilityType.TOGGLE.value: self.init_toggle,
            CapabilityType.VIDEO_STREAM.value: self.init_video_stream,
        }
        constructor_map[self.type]()
        super(Capability, self).save(**kwargs)

    def init_color_settings(self):
        self.parameters = {}
        if self.color_model:
            self.parameters["color_model"] = self.color_model  # hsv/rgb
            if self.color_model == ColorModel.HSV.value:
                if not self.state:
                    self.state.append({
                        "instance": "hsv",
                        "value": {
                            "h": 0,
                            "s": 0,
                            "v": 0
                        }
                    })
            elif self.color_model == ColorModel.RGB.value:
                if not self.state:
                    self.state.append({
                        "instance": "rgb",
                        "value": 0
                    })

        if self.temp_k_max and self.temp_k_min:
            self.parameters['temperature_k'] = {"min": self.temp_k_min, "max": self.temp_k_max}
            if not self.state:
                self.state.append({
                    "instance": "temperature_k",
                    "value": self.temp_k_min or self.temp_k_max
                })

    def init_mode(self):
        self.parameters["instance"] = self.mode_instance
        self.parameters["modes"] = [{"value": x} for x in self.modes]
        if not self.state:
            self.state.append({
                "instance": self.mode_instance,
                "value": self.parameters['modes'][0]['value']
            })

    def init_on_off(self):
        if not self.retrievable:
            if self.split:
                self.parameters = {
                    "split": self.split
                }
        if not self.state:
            self.state.append({
                "instance": "on",
                "value": False
            })

    def init_range(self):
        self.parameters["instance"] = self.range_instance
        if self.unit:
            self.parameters["unit"] = self.unit

        if self.random_access is not None:
            self.parameters["random_access"] = self.random_access

        if self.range_min or self.range_max or self.range_precision:
            self.parameters["range"] = {'min': self.range_min, 'max': self.range_max}
            if self.range_precision is not None:
                self.parameters["range"]['precision'] = self.range_precision

        if not self.state:
            self.state.append({
                "instance": self.range_instance,
                "value": self.range_min if self.range_min else 0
            })

    def init_toggle(self):
        self.parameters["instance"] = self.toggle_instance
        if not self.state:
            self.state.append({
                "instance": self.toggle_instance,
                "value": False
            })

    def init_video_stream(self):
        self.retrievable = False
        self.reportable = False
        self.parameters = {
            "protocols": [self.protocol]
        }
        if not self.state:
            self.state.append({
                "instance": self.protocol,
                "value": ""
            })

    def set_state(self, new_state):
        # ToDo: test color
        yandex_logger.info("Обновление состояния устройства")
        error = None
        try:
            _self_state = []
            for state_item in self.state:
                if state_item['instance'] == new_state['instance']:
                    _self_state.append(new_state)
                    self.update_mqtt_state(new_state['value'])
                else:
                    _self_state.append(state_item)
            self.state = _self_state
            self.save()
        except Exception as e:
            yandex_logger.exception(f"Ошибка обновления состояния способности \"{self}\"")
            error = f"Ошибка какая-то\n{str(e)}"

        data = {
            "type": self.type,
            "state": {
                "instance": new_state['instance']
            }
        }
        if not error:
            data['state']['action_result'] = {
                "status": Status.DONE.value,
            }
        else:
            data['state']["action_result"] = {
                "status": Status.ERROR.value,
                "error_message": error
            }
        yandex_logger.debug(f"Новое состояние способности \"{self}\": {new_state}")

        return data

    def update_mqtt_state(self, new_state):
        from ..mqtt.MqttClient import MqttClient
        client = MqttClient(self.mqtt_config)
        client.publish_message(self.command_topic, new_state)

    def __str__(self):
        return self.name if self.name else str(self.pk)

    class Meta:
        verbose_name = "умение"
        verbose_name_plural = "умения"


class Property(BaseAbilityModel, models.Model):
    # Общее
    type = models.CharField("Тип устройства", max_length=100, choices=PropertyTypeChoices)
    device = models.ForeignKey(Device, verbose_name="Устройство", related_name="properties", on_delete=models.CASCADE)

    # Float
    float_instance = models.CharField("Название функции для свойства", max_length=50, choices=FloatInstanceChoices,
                                      blank=True)
    unit = models.CharField("Единица измерения", max_length=50, choices=FloatUnitChoices, blank=True)
    # Event
    event_instance = models.CharField("Название функции для свойства", max_length=50, choices=EventInstanceChoices,
                                      blank=True)
    events = ChoiceArrayField(models.CharField("События", max_length=50, choices=EventChoices), blank=True)

    def save(self, *args, **kwargs):
        constructor_map = {
            PropertyType.FLOAT.value: self.init_float,
            PropertyType.EVENT.value: self.init_event,
        }
        constructor_map[self.type]()
        super(Property, self).save(*args, **kwargs)

    def init_float(self):
        self.parameters["instance"] = self.float_instance
        if self.unit:
            self.parameters["unit"] = self.unit

        if not self.state:
            self.state.append({
                "instance": self.float_instance,
                "value": 0
            })

    def init_event(self):
        self.parameters["instance"] = self.event_instance
        self.parameters["events"] = [{"value": x} for x in self.events]
        if not self.state:
            self.state.append({
                "instance": self.event_instance,
                "value": self.parameters['events'][0]['value']
            })

    def __str__(self):
        return self.name if self.name else str(self.pk)

    class Meta:
        verbose_name = "свойство"
        verbose_name_plural = "свойства"
