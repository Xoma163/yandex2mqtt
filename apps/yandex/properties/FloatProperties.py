from apps.yandex.properties.FloatPropertiesUtils.Unit import Unit
from apps.yandex.properties.FloatPropertiesUtils.Instance import Instance
from apps.yandex.properties.Properties import Properties


class FloatProperties(Properties):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/float.html
    """

    ALLOWED_UNITS_BY_INSTANCE = {
        Instance.AMPERAGE: [Unit.AMPERE],
        Instance.BATTERY_LEVEL: [Unit.PERCENT],
        Instance.CO2_LEVEL: [Unit.PPM],
        Instance.HUMIDITY: [Unit.PERCENT],
        Instance.ILLUMINATION: [Unit.LUX],
        Instance.PM1_DENSITY: [Unit.MCG_M3],
        Instance.PM2_5_DENSITY: [Unit.MCG_M3],
        Instance.PM10_DENSITY: [Unit.MCG_M3],
        Instance.POWER: [Unit.WATT],
        Instance.PRESSURE: [Unit.ATM, Unit.PASCAL, Unit.BAR, Unit.MMHG],
        Instance.TEMPERATURE: [Unit.KELVIN, Unit.CELSIUS],
        Instance.TVOC: [Unit.MCG_M3],
        Instance.VOLTAGE: [Unit.VOLT],
        Instance.WATER_LEVEL: [Unit.PERCENT],
    }

    def __init__(self, instance: Instance, unit: Unit = None, **kwargs):
        super().__init__(**kwargs)

        if instance:
            if not isinstance(instance, Instance):
                raise RuntimeError("instance must be Instance instance")
            self.parameters["instance"] = instance.value

        if unit:
            if not isinstance(unit, Unit):
                raise RuntimeError("unit must be Unit instance")
            if unit not in self.ALLOWED_UNITS_BY_INSTANCE[instance]:
                allowed_units_str = ", ".join([x.value for x in self.ALLOWED_UNITS_BY_INSTANCE[instance]])
                raise RuntimeError(f"unit must be in {allowed_units_str} for instance {instance}")
            self.parameters["unit"] = unit.value
