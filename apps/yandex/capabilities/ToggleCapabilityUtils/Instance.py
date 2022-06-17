from enum import Enum


class Instance(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/toggle-instance.html
    """
    BACKLIGHT = "backlight"  # Подсветка
    CONTROLS_LOCKED = "controls_locked"  # Детский режим
    IONIZATION = "ionization"  # Ионизация
    KEEP_WARM = "keep_warm"  # Поддержание тепла
    MUTE = "mute"  # Выключение звука
    OSCILLATION = "oscillation"  # Вращение
    PAUSE = "pause"  # Пауза
