from enum import Enum


class Instance(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/range-instance.html
    """
    BRIGHTNESS = "brightness"
    CHANNEL = "channel"
    HUMIDITY = "humidity"
    OPEN = "open"
    TEMPERATURE = "temperature"
    VOLUME = "volume"
