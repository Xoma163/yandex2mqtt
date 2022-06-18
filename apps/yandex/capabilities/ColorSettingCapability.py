from apps.yandex.capabilities.Capability import Capability
from apps.yandex.capabilities.ColorSettingCapabilityUtils.ColorModel import ColorModel


class ColorSettingCapability(Capability):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/color_setting.html
    """

    MIN_K_TEMP = 2000
    MAX_K_TEMP = 9000

    def __init__(self, color_model: ColorModel = None, temp_k_min: int = None, temp_k_max: int = None, **kwargs):
        super().__init__(**kwargs)
        self.type = "devices.capabilities.color_setting"

        self.color_model = color_model
        self.temp_k_min = temp_k_min
        self.temp_k_max = temp_k_max

        if color_model:
            if not isinstance(color_model, ColorModel):
                raise RuntimeError("color_model must be ColorMode instance")
            self.parameters = {
                "color_modell": color_model.value,  # hsv/rgb
            }
            if color_model == ColorModel.HSV:
                self.value = {'h': 0, 's': 0, 'v': 0}  # [0; 360] [0; 100] [0; 100]
            elif color_model == ColorModel.RGB:
                self.value = 0  # [0; 16777215]
        else:
            if temp_k_min and temp_k_min:
                self.parameters = {'temperature_k': {}}
            elif temp_k_min or temp_k_max:
                self.parameters['temperature_k'] = None

            if temp_k_min:
                self.value = self.MIN_K_TEMP
                if not isinstance(temp_k_min, int):
                    raise RuntimeError("temp_k_min must be int")
                if temp_k_min < self.MIN_K_TEMP or temp_k_min > self.MAX_K_TEMP:
                    raise RuntimeError(f"temp_k_min must be in range {self.MIN_K_TEMP}-{self.MAX_K_TEMP}")
                if not temp_k_max:
                    self.parameters['temperature_k'] = temp_k_min
                else:
                    self.parameters['temperature_k']['min'] = temp_k_min

            if temp_k_max:
                self.value = self.MAX_K_TEMP
                if not isinstance(temp_k_max, int):
                    raise RuntimeError("temp_k_max must be int")
                if temp_k_min < self.MIN_K_TEMP or temp_k_min > self.MAX_K_TEMP:
                    raise RuntimeError(f"temp_k_min must be in range {self.MIN_K_TEMP}-{self.MAX_K_TEMP}")
                if not temp_k_min:
                    self.parameters['temperature_k'] = temp_k_min
                else:
                    self.parameters['temperature_k']['max'] = temp_k_max

            if temp_k_min and temp_k_min:
                if temp_k_max < temp_k_min:
                    raise RuntimeError("temp_k_max must be higher than temp_k_min")

        # self.parameters["color_scene"] = []

        # "alarm",
        # "alice",
        # "candle",
        # "dinne",
        # "fantasy",
        # "garland",
        # "jungle",
        # "movie",
        # "neon",
        # "night",
        # "ocean",
        # "party",
        # "reading",
        # "rest",
        # "romance",
        # "siren",
        # "sunrise",
        # "sunset",
