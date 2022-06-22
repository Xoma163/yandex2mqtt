import threading

from apps.mqtt.MqttClient import MqttClient
from apps.mqtt.models import MqttConfig


def start_client(config):
    mqtt = MqttClient(config)
    mqtt.subscribe()
    mqtt.loop()


def run_background_mqtt_listeners():
    for config in MqttConfig.objects.all():
        threading.Thread(target=start_client, args=(config,)).start()
