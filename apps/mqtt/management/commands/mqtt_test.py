from django.core.management import BaseCommand


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        pass
        
        # mqtt = MqttClient()
