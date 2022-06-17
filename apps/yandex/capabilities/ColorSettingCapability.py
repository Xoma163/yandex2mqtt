from apps.yandex.capabilities.Capability import Capability
from apps.yandex.capabilities.ColorSettingCapabilityUtils.ColorMode import ColorMode


class ColorSettingCapability(Capability):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/color_setting.html
    """

    def __init__(self, color_mode: ColorMode, temp_k_min: int = None, temp_k_max: int = None, **kwargs):
        super().__init__(**kwargs)
        self.type = "devices.capabilities.color_setting"

        if not isinstance(color_mode, ColorMode):
            raise RuntimeError("color_mode must be ColorMode instance")

        self.parameters = {
            "color_model": color_mode.value,  # hsv/rgb
        }
        if temp_k_min or temp_k_max:
            self.parameters['temperature_k'] = {}
        if temp_k_min:
            if not isinstance(temp_k_min, int):
                raise RuntimeError("temp_k_min must be int")
            if temp_k_min < 2000 or temp_k_min > 9000:
                raise RuntimeError("temp_k_min must be in range 2000-9000")
            if temp_k_min:
                self.parameters['temperature_k']['min'] = temp_k_min

        if temp_k_max:
            if not isinstance(temp_k_max, int):
                raise RuntimeError("temp_k_max must be int")
            if temp_k_max < 2000 or temp_k_max > 9000:
                raise RuntimeError("temp_k_max must be in range 2000-9000")
            if temp_k_max:
                self.parameters['temperature_k']['max'] = temp_k_max

        if temp_k_min and temp_k_max and temp_k_max < temp_k_min:
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
