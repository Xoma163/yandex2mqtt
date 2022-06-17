from enum import Enum


class Unit(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/range-instance.html
    """
    PERCENT = "unit.percent"
    CELSIUS = "unit.temperature.celsius"
    KELVIN = "unit.temperature.kelvin"
