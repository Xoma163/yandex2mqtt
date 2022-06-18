from apps.yandex.properties.EventPropertiesUtils.Event import Event
from apps.yandex.properties.EventPropertiesUtils.Instance import Instance
from apps.yandex.properties.Property import Property


class EventProperties(Property):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/event.html
    """
    ALLOWED_EVENTS_BY_INSTANCE = {
        Instance.VIBRATION: [Event.TILT, Event.FALL, Event.VIBRATION],
        Instance.OPEN: [Event.OPENED, Event.CLOSED],
        Instance.BUTTON: [Event.CLICK, Event.DOUBLE_CLICK, Event.LONG_PRESS],
        Instance.MOTION: [Event.DETECTED, Event.NOT_DETECTED],
        Instance.SMOKE: [Event.DETECTED, Event.NOT_DETECTED, Event.HIGH],
        Instance.GAS: [Event.DETECTED, Event.NOT_DETECTED, Event.HIGH],
        Instance.BATTERY_LEVEL: [Event.LOW, Event.HIGH],
        Instance.WATER_LEVEL: [Event.LOW, Event.NORMAL],
        Instance.WATER_LEAR: [Event.DRY, Event.LEAK]
    }

    def __init__(self, instance: Instance, event: Event, **kwargs):
        super().__init__(**kwargs)

        if instance:
            if not isinstance(instance, Instance):
                raise RuntimeError("instance must be Instance instance")
            self.parameters["instance"] = instance.value

        if event:
            if not isinstance(event, Event):
                raise RuntimeError("event must be Event instance")
            if event not in self.ALLOWED_EVENTS_BY_INSTANCE[instance]:
                allowed_events_str = ", ".join([x.value for x in self.ALLOWED_EVENTS_BY_INSTANCE[instance]])
                raise RuntimeError(f"event must be in {allowed_events_str} for instance {instance}")
            self.parameters["event"] = event.value
