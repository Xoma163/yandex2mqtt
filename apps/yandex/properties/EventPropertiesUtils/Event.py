from enum import Enum


class Event(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/event-instance.html
    """

    TILT = "tilt"  # переворачивание
    FALL = "fall"  # падение
    VIBRATION = "vibration"  # вибрация
    OPENED = "opened"  # открыто
    CLOSED = "closed"  # закрыто
    CLICK = "click"  # одиночное нажатие
    DOUBLE_CLICK = "double_click"  # двойное нажатие
    LONG_PRESS = "long_press"  # долгое нажатие
    DETECTED = "detected"  # обнаружено
    NOT_DETECTED = "not_detected"  # не обнаружено
    HIGH = "high"  # высокий уровень
    LOW = "low"  # низкий
    NORMAL = "normal"  # нормальный
    DRY = "dry"  # нет протечки
    LEAK = "leak"  # протечка
