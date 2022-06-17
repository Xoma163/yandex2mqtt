from django.core.management import BaseCommand

from apps.yandex.capabilities.RangeCapability import RangeCapability
from apps.yandex.capabilities.RangeCapabilityUtils.Instance import Instance
from apps.yandex.capabilities.RangeCapabilityUtils.Unit import Unit


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        pass
        
        # mqtt = MqttClient()
