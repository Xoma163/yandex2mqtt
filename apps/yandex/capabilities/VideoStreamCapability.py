from apps.yandex.capabilities.Capability import Capability
from apps.yandex.capabilities.VideoCapabilityUtils.Protocol import Protocol


class VideoStreamCapability(Capability):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/video_stream.html
    """

    def __init__(self, protocol: Protocol, **kwargs):
        super().__init__(**kwargs)
        self.type = "devices.capabilities.video_stream"

        self.protocol = protocol

        if not isinstance(protocol, Protocol):
            raise RuntimeError("protocol must be Protocol instance")
        self.parameters = {
            "protocols": [protocol.value]
        }

    def get_state(self):
        raise RuntimeError("cant get this method for VideoStream capability")
