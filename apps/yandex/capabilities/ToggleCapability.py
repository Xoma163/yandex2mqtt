from apps.yandex.capabilities.Capability import Capability
from apps.yandex.capabilities.ToggleCapabilityUtils.Instance import Instance


class ToggleCapability(Capability):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/toggle.html
    """

    def __init__(self, instance: Instance,**kwargs):
        super().__init__(**kwargs)
        self.type = "devices.capabilities.toggle"

        if not isinstance(instance, Instance):
            raise RuntimeError("instance must be Instance instance")
        self.parameters["instance"] = instance.value
