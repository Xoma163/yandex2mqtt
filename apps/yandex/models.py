from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .consts import Status, ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE
from .model_consts import *
from ..mqtt.models import MqttConfig


class Room(models.Model):
    name = models.CharField("Комната", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class CapabilityMode(models.Model):
    mode = models.CharField("mode", max_length=50, choices=ModeChoices)

    def __str__(self):
        return self.get_mode_display()

    class Meta:
        verbose_name = "Функция(Mode) возможности"
        verbose_name_plural = "Функции(Mode) возможности"


class Capability(models.Model):
    # Общее
    name = models.CharField("Название", max_length=100, blank=True)
    type = models.CharField("Тип устройства", max_length=100, choices=CapabilityTypeChoices)
    parameters = models.JSONField("Параметры", default=dict, editable=False)
    retrievable = models.BooleanField("Включенное оповещение", default=True,
                                      help_text="Признак включенного оповещения об изменении состояния умения при помощи сервиса уведомлений")
    reportable = models.BooleanField("Доступен ли запрос состояния", default=True,
                                     help_text="Доступен ли для данного умения устройства запрос состояния")
    state = models.JSONField(default=list, help_text="Стейт", blank=True)
    # mqtt
    mqtt_config = models.ForeignKey(MqttConfig, verbose_name="Конфигурация MQTT", on_delete=models.SET_NULL, null=True)
    command_topic = models.CharField("Топик для команд", max_length=100)
    state_topic = models.CharField("Топик для состояния", max_length=100)
    # ColorSetting
    color_model = models.CharField("Цветовая модель", max_length=10, choices=ColorModelChoices, blank=True)
    temp_k_min = models.PositiveIntegerField("Минимальная температура света", null=True, blank=True,
                                             validators=[MinValueValidator(2000), MaxValueValidator(9000)])
    temp_k_max = models.PositiveIntegerField("Максимальная температура света", null=True, blank=True,
                                             validators=[MinValueValidator(2000), MaxValueValidator(9000)])
    # Mode
    mode_instance = models.CharField("instance", max_length=50, choices=ModeInstanceChoices, blank=True)
    modes = models.ManyToManyField(CapabilityMode, blank=True)
    # OnOff
    split = models.BooleanField("split", blank=True,
                                help_text="За включение/выключение устройства у провайдера отвечают разные команды")
    # Range
    range_instance = models.CharField("instance", max_length=50, choices=RangeInstanceChoices, blank=True)
    unit = models.CharField("Единица измерения", max_length=50, choices=RangeUnitChoices, blank=True)
    random_access = models.BooleanField("Произвольные значения", blank=True,
                                        help_text="Если эта возможность выключена, пользователю будет доступно только последовательное изменение значений — в большую или меньшую сторону. Например, изменение громкости телевизора при работе через ИК пульт.")
    range_min = models.PositiveIntegerField("Минимальное значение", null=True, blank=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(100)])
    range_max = models.PositiveIntegerField("Максимальное значение", null=True, blank=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(100)])
    range_precision = models.PositiveIntegerField("Шаг", blank=True, null=True)
    # Toggle
    toggle_instance = models.CharField("instance", max_length=50, choices=ToggleInstanceChoices, blank=True)
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
        super(Capability, self).save()

    def init_color_settings(self):
        if not self.color_model and not self.temp_k_min and not self.temp_k_max:
            raise RuntimeError(f"color_model or temp_k_min or temp_k_max must be provided for type {self.type}")
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

        if self.temp_k_min and self.temp_k_max is None or self.temp_k_max and self.temp_k_min is None:
            raise RuntimeError("temp_k_min and temp_k_max must be provided together")

        if self.temp_k_max and self.temp_k_min:
            if self.temp_k_max < self.temp_k_min:
                raise RuntimeError("temp_k_max must be higher than temp_k_min")
            self.parameters['temperature_k'] = {"min": self.temp_k_min, "max": self.temp_k_max}
            if not self.state:
                self.state.append({
                    "instance": "temperature_k",
                    "value": self.temp_k_min or self.temp_k_max
                })

    def init_mode_post(self):
        if self.modes.count() == 0:
            raise RuntimeError(f"mode_instance and modes must be provided for type {self.type}")
        self.parameters["modes"] = [{"value": x.mode} for x in self.modes.all()]
        if not self.state:
            self.state.append({
                "instance": self.mode_instance,
                "value": self.parameters['modes'][0]['value']
            })

    def init_mode(self):
        if not self.mode_instance:
            raise RuntimeError(f"mode_instance and modes must be provided for type {self.type}")
        self.parameters["instance"] = self.mode_instance

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
        if not self.range_instance:
            raise RuntimeError(f"range_instance must be provided for type {self.type}")

        self.parameters["instance"] = self.range_instance

        if self.unit:
            if self.unit not in ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE[self.range_instance]:
                allowed_units_str = ", ".join(ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE[self.range_instance])
                raise RuntimeError(f"unit must be in {allowed_units_str} for instance {self.range_instance}")
            self.parameters["unit"] = self.unit

        if self.random_access is not None:
            self.parameters["random_access"] = self.random_access

        if self.range_min or self.range_max or self.range_precision:
            if self.range_min and self.range_max is None or self.range_max and self.range_min is None:
                raise RuntimeError("range_min and range_max must be provided together")
            if self.range_min > self.range_max:
                raise RuntimeError("range_min must be lower that range_max")

            self.parameters["range"] = {'min': self.range_min, 'max': self.range_max}

            if self.range_precision is not None:
                if self.range_min is None or self.range_max is None:
                    raise RuntimeError("range_precision, range_min and range_max must be provided together")

                self.parameters["range"]['precision'] = self.range_precision

        if not self.state:
            self.state.append({
                "instance": self.range_instance,
                "value": self.range_min if self.range_min else 0
            })

    def init_toggle(self):
        if not self.toggle_instance:
            raise RuntimeError(f"toggle_instance must be provided for type {self.type}")
        self.parameters["instance"] = self.toggle_instance
        if not self.state:
            self.state.append({
                "instance": self.toggle_instance,
                "value": False
            })

    def init_video_stream(self):
        self.retrievable = False
        self.reportable = False
        if not self.protocol:
            raise RuntimeError(f"protocol must be provided for type {self.type}")

        self.parameters = {
            "protocols": [self.protocol]
        }
        if not self.state:
            self.state.append({
                "instance": self.protocol,
                "value": ""
            })

    def get_for_device_list(self):
        return {
            'type': self.type,
            'retrievable': self.retrievable,
            'reportable': self.reportable,
            'parameters': self.parameters,
        }

    def set_state(self, new_state):
        # ToDo: mqtt
        error = None
        try:
            _self_state = []
            for state_item in self.state:
                if state_item['instance'] == new_state['instance']:
                    _self_state.append(new_state)
                else:
                    _self_state.append(state_item)
            self.state = _self_state
            self.save()
        except Exception as e:
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

        return data

    def __str__(self):
        return self.name if self.name else str(self.pk)

    class Meta:
        verbose_name = "Возможность"
        verbose_name_plural = "Возможности"


class Device(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name="Автор", on_delete=models.CASCADE, related_name="devices")
    name = models.CharField("Название", max_length=100)
    type = models.CharField("Тип", choices=DeviceTypeChoices, max_length=50,
                            help_text="https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, verbose_name="Комната", null=True, blank=True)
    description = models.TextField("Описание", max_length=100, blank=True)
    custom_data = models.JSONField(default=dict, verbose_name="Кастомные данные", blank=True)
    capabilities = models.ManyToManyField(Capability, verbose_name="Возможности")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

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
        # ToDo: new state
        if self.capabilities:
            for capability in self.capabilities.all():
                for value in new_values:
                    if value['type'] == capability.type:
                        data['capabilities'].append(capability.set_state(value['state']))
                        break
        return data
