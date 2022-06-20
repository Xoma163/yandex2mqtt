import paho.mqtt.client as mqtt
import json

from apps.mqtt.models import MqttConfig


class MqttClient:
    def __init__(self, config: MqttConfig):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.username_pw_set(config.login, config.password)
        self.client.connect(config.url, config.port, 60)

    def loop(self):
        self.client.loop_forever()
        self.client.on_message = self.on_message

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc != 0:
            raise RuntimeError(f"MqttClient connected with error_code={rc}")
        client.subscribe("#")

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        decoded_msg = msg.payload.decode()
        self.handle_message(topic, decoded_msg)

    @staticmethod
    def handle_message(topic, msg):
        print(topic)
        print(msg)

    def publish_message(self, topic, payload):
        if isinstance(payload, dict):
            _payload = json.dumps(payload)
        else:
            _payload = payload
        self.client.publish(topic, _payload)
