from enum import Enum


class Instance(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/event-instance.html
    """

    VIBRATION = "vibration"  # Отображение событий физического воздействия: вибрация, падение, переворачивание.
    OPEN = "open"  # Отображение событий открытия/закрытия дверей, окон и т. п.
    BUTTON = "button"  # Отображение событий нажатия кнопки.
    MOTION = "motion"  # Отображение событий, связанных с наличием движения в области действия датчика.
    SMOKE = "smoke"  # Отображение событий наличия дыма в помещении.
    GAS = "gas"  # Отображение событий наличия газа в помещении.
    BATTERY_LEVEL = "battery_level"  # Отображение событий заряда батареи.
    WATER_LEVEL = "water_level"  # Отображение событий, связанных с уровнем воды.
    WATER_LEAR = "water_leak"  # Отображение событий протечки воды.

