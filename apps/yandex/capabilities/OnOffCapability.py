from apps.yandex.capabilities.Capability import Capability


class OnOffCapability(Capability):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/on_off.html
    """

    def __init__(self, split: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.type = "devices.capabilities.on_off"
        self.value = False

        self.split = split

        if not self.retrievable:
            if split:
                if not isinstance(split, bool):
                    raise RuntimeError("split must be bool")
                self.parameters = {
                    "split": split
                }
