import threading
from django.apps import AppConfig


class MqttConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.mqtt'

    def ready(self):
        from .models import MqttConfig as MqttConfigModel
        for config in MqttConfigModel.objects.all():
            threading.Thread(target=self.start_client, args=(config,)).start()

    @staticmethod
    def start_client(config):
        from .MqttClient import MqttClient
        mqtt = MqttClient(config)
        mqtt.subscribe()
        mqtt.loop()
