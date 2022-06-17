from enum import Enum


class Unit(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/float-instance.html
    """

    AMPERE = "unit.ampere"
    PERCENT = "unit.percent"
    PPM = "unit.ppm"
    LUX = "unit.illumination.lux"
    MCG_M3 = "unit.density.mcg_m3"
    WATT = "unit.watt"
    ATM = "unit.pressure.atm"
    PASCAL = "unit.pressure.pascal"
    BAR = "unit.pressure.bar"
    MMHG = "unit.pressure.mmhg"
    CELSIUS = "unit.temperature.celsius"
    KELVIN = "unit.temperature.kelvin"
    VOLT = "unit.volt"
