from enum import Enum


class Protocol(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/video_stream.html
    """
    HLS = "hls"
    PROGRESSIVE_MP4 = "progressive_mp4"
