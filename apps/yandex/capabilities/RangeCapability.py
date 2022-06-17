from apps.yandex.capabilities.Capability import Capability
from apps.yandex.capabilities.RangeCapabilityUtils.Instance import Instance
from apps.yandex.capabilities.RangeCapabilityUtils.Unit import Unit


class RangeCapability(Capability):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/range.html
    """

    ALLOWED_UNITS_BY_INSTANCE = {
        Instance.BRIGHTNESS: [Unit.PERCENT],
        Instance.CHANNEL: [],
        Instance.HUMIDITY: [Unit.PERCENT],
        Instance.OPEN: [Unit.PERCENT],
        Instance.TEMPERATURE: [Unit.KELVIN, Unit.CELSIUS],
        Instance.VOLUME: [Unit.PERCENT]
    }

    def __init__(self, instance: Instance, unit: Unit = None, random_access: bool = True,
                 range_min: float = None, range_max: float = None, range_precision: float = None,**kwargs):
        super().__init__(**kwargs)
        self.type = "devices.capabilities.range"

        if instance:
            if not isinstance(instance, Instance):
                raise RuntimeError("instance must be Instance instance")
            self.parameters["instance"] = instance.value

        if unit:
            if not isinstance(unit, Unit):
                raise RuntimeError("unit must be Unit instance")
            if unit not in self.ALLOWED_UNITS_BY_INSTANCE[instance]:
                allowed_units_str = ", ".join(self.ALLOWED_UNITS_BY_INSTANCE[instance])
                raise RuntimeError(f"unit must be in {allowed_units_str} for instance {instance}")
            self.parameters["unit"] = unit.value

        if random_access:
            if not isinstance(random_access, bool):
                raise RuntimeError("random_access must be bool instance")
            self.parameters["random_access"] = random_access

        if range_min or range_max or range_precision:
            self.parameters["range"] = {}

        if range_min:
            if not isinstance(range_min, float) and not isinstance(range_min, int):
                raise RuntimeError("range_min must be float/int instance")
            self.parameters["range"]['range_min'] = range_min

        if range_max:
            if not isinstance(range_max, float) and not isinstance(range_max, int):
                raise RuntimeError("range_max must be float/int instance")
            self.parameters["range"]['range_max'] = range_max

        if range_precision:
            if not isinstance(range_precision, float) and not isinstance(range_precision, int):
                raise RuntimeError("range_precision must be float/int instance")
            self.parameters["range"]['range_precision'] = range_precision

        """
        instance
        unit
        random_access
        range
        """
