from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .consts import  Status, ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE
from .model_consts import *


class Room(models.Model):
    name = models.CharField("Комната", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class Capability(models.Model):
    # @formatter:off

    # Общее
    author = models.ForeignKey(get_user_model(), verbose_name="Автор", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=100, blank=True)
    type = models.CharField("Тип устройства", max_length=100, choices=CapabilityTypeChoices)
    parameters = models.JSONField("Параметры", default=dict, editable=False)
    retrievable = models.BooleanField("Включенное оповещение", default=True, help_text="Признак включенного оповещения об изменении состояния умения при помощи сервиса уведомлений")
    reportable = models.BooleanField("Доступен ли запрос состояния", default=False, help_text="Доступен ли для данного умения устройства запрос состояния")
    value = models.JSONField(default=dict, help_text="Изначальное значение", blank=True)
    # mqtt

    # ColorSetting
    color_model = models.CharField("Цветовая модель", max_length=10, choices=ColorModel.choices, blank=True)
    temp_k_min = models.PositiveIntegerField("Минимальная температура света", null=True,blank=True, validators=[MinValueValidator(2000), MaxValueValidator(9000)])
    temp_k_max = models.PositiveIntegerField("Максимальная температура света", null=True, blank=True, validators=[MinValueValidator(2000), MaxValueValidator(9000)])
    # Mode
    mode_instance = models.CharField("instance", max_length=50, choices=ModeInstanceChoices, blank=True)
    modes = ArrayField(models.CharField("mode", max_length=50, choices=ModeChoices), blank=True)
    # OnOff
    split = models.BooleanField("split", blank=True, help_text="За включение/выключение устройства у провайдера отвечают разные команды")
    # Range
    range_instance = models.CharField("instance", max_length=50, choices=RangeInstanceChoices, blank=True)
    unit = models.CharField("Единица измерения", max_length=50, choices=RangeUnitChoices, blank=True)
    random_access = models.BooleanField("Произвольные значения", blank=True, help_text="Если эта возможность выключена, пользователю будет доступно только последовательное изменение значений — в большую или меньшую сторону. Например, изменение громкости телевизора при работе через ИК пульт.")
    range_min = models.PositiveIntegerField("Минимальное значение", null=True, blank=True,  validators=[MinValueValidator(1), MaxValueValidator(100)])
    range_max = models.PositiveIntegerField("Максимальное значение", null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    range_precision = models.PositiveIntegerField("Шаг", blank=True, null=True)
    # Toggle
    toggle_instance = models.CharField("instance", max_length=50, choices=ToggleInstanceChoices, blank=True)
    # VideoStream
    protocol = models.CharField("Протокол", max_length=50, choices=Protocol.choices, blank=True)

    # @formatter:on

    def save(self, **kwargs):
        self.parameters = {}
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
        if not self.color_model or not self.temp_k_min or not self.temp_k_max:
            raise RuntimeError(f"color_model or temp_k_min or temp_k_max must be provided for type {self.type}")

        if self.color_model:
            self.parameters = {
                "color_model": self.color_model,  # hsv/rgb
            }
            if self.color_model == ColorModel.HSV:
                self.value = {'h': 0, 's': 0, 'v': 0}  # [0; 360] [0; 100] [0; 100]
            elif self.color_model == ColorModel.RGB:
                self.value = 0  # [0; 16777215]
        else:
            if self.temp_k_min and self.temp_k_min:
                if self.temp_k_max < self.temp_k_min:
                    raise RuntimeError("temp_k_max must be higher than temp_k_min")
                self.parameters = {
                    'temperature_k': {
                        'min': self.temp_k_min,
                        'max': self.temp_k_max
                    }}
            elif self.temp_k_min:
                self.parameters['temperature_k'] = self.temp_k_min
            elif self.temp_k_max:
                self.parameters['temperature_k'] = self.temp_k_max

    def init_mode(self):
        if not self.mode_instance and not self.modes:
            raise RuntimeError(f"mode_instance and modes must be provided for type {self.type}")

        self.parameters["instance"] = self.mode_instance
        self.parameters["modes"] = self.modes

    def init_on_off(self):
        if not self.retrievable:
            if self.split:
                self.parameters = {
                    "split": self.split
                }

    def init_range(self):
        if not self.range_instance:
            raise RuntimeError(f"range_instance must be provided for type {self.type}")

        self.parameters["instance"] = self.range_instance

        if self.unit:
            if self.unit not in ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE[self.range_instance]:
                allowed_units_str = ", ".join(ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE[self.range_instance])
                raise RuntimeError(f"unit must be in {allowed_units_str} for instance {self.range_instance}")
            self.parameters["unit"] = self.unit

        if self.random_access:
            self.parameters["random_access"] = self.random_access

        if self.range_min or self.range_max or self.range_precision:
            self.parameters["range"] = {}

        if self.range_min:
            self.parameters["range"]['range_min'] = self.range_min

        if self.range_max:
            self.parameters["range"]['range_max'] = self.range_max

        if self.range_precision:
            self.parameters["range"]['range_precision'] = self.range_precision

    def init_toggle(self):
        if not self.toggle_instance:
            raise RuntimeError(f"toggle_instance must be provided for type {self.type}")
        self.parameters["instance"] = self.toggle_instance

    def init_video_stream(self):
        if not self.protocol:
            raise RuntimeError(f"protocol must be provided for type {self.type}")

        self.parameters = {
            "protocols": [self.protocol]
        }

    def get_for_device_list(self):
        return {
            'type': self.type,
            'retrievable': self.retrievable,
            'reportable': self.reportable,
            'parameters': self.parameters,
        }

    def get_state(self):
        return {
            "type": self.type,
            "state": {
                "instance": "on",
                "value": self.value,
            }
        }

    def switch_state(self, new_value):
        # ToDo: switch with new_value
        error = None
        try:
            self.value = new_value
        except Exception as e:
            error = f"Ошибка какая-то\n{str(e)}"

        data = {
            "type": self.type,
            "state": {
                "instance": "on"
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
    name = models.CharField("Название", max_length=100)
    type = models.CharField("Тип", choices=DeviceTypeChoices, max_length=50,
                            help_text="https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField("Описание", max_length=100, blank=True)
    custom_data = models.JSONField(default=dict, help_text="Кастомные данные", blank=True)
    capabilities = models.ManyToManyField(Capability)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"
