from enum import Enum


class Instance(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/float-instance.html
    """

    AMPERAGE = "amperage"  # Отображение текущего потребления тока.
    BATTERY_LEVEL = "battery_level"  # Отображение уровня заряда аккумулятора.
    CO2_LEVEL = "co2_level"  # Отображение показаний уровня углекислого газа.
    HUMIDITY = "humidity"  # Отображение показаний влажности.
    ILLUMINATION = "illumination"  # Отображение уровня освещенности.
    PM1_DENSITY = "pm1_density"  # Отображение уровня загрязнения воздуха частицами PM1.
    PM2_5_DENSITY = "pm2.5_density"  # Отображение уровня загрязнения воздуха частицами PM2.5.
    PM10_DENSITY = "pm10_density"  # Отображение уровня загрязнения воздуха частицами PM10.
    POWER = "power"  # Отображение текущей потребляемой мощности.
    PRESSURE = "pressure"  # Отображение давления.
    TEMPERATURE = "temperature"  # Отображение показаний температуры.
    TVOC = "tvoc"  # Отображение уровня загрязнения воздуха органическими веществами.
    VOLTAGE = "voltage"  # Отображение текущего напряжения.
    WATER_LEVEL = "water_level"  # Отображение показаний уровня воды.
