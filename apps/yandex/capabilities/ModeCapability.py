from typing import List

from apps.yandex.capabilities.Capability import Capability
from apps.yandex.capabilities.ModeCapabilityUtils.Instance import Instance
from apps.yandex.capabilities.ModeCapabilityUtils.Mode import Mode


class ModeCapability(Capability):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/mode.html
    """

    def __init__(self, instance: Instance, modes: List[Mode], **kwargs):
        super().__init__(**kwargs)
        self.type = "devices.capabilities.mode"

        self.instance = instance
        self.modes = modes

        if not isinstance(instance, Instance):
            raise RuntimeError("instance must be Instance instance")
        self.parameters["instance"] = instance.value

        for mode in modes:
            if not isinstance(mode, Mode):
                raise RuntimeError("mode in modes list must be Mode instance")
        self.parameters["modes"] = [x.value for x in modes]
        self.value = modes[0].value
