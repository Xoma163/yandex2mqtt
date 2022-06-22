import paho.mqtt.client as mqtt
import json

from django.db.models.signals import post_save, post_delete

from apps.yandex.consts import PropertyType, ALLOWED_EVENTS_BY_EVENT_INSTANCE, CapabilityType, TF_TRANSLATOR
from jsonpath_ng import parse

from apps.mqtt.models import MqttConfig
from apps.yandex.models import Capability, Property


class MqttClient:

    def __init__(self, config: MqttConfig):
        self._config = config
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(config.login, config.password)
        self.client.connect(config.url, config.port, 60)

        self.topic_devices = {}

    def loop(self):
        self.client.loop_forever()

    def subscribe(self):
        for cap in Capability.objects.filter(mqtt_config=self._config):
            self.sub_topic(cap.state_topic, cap)

        for prop in Property.objects.filter(mqtt_config=self._config):
            self.sub_topic(prop.state_topic, prop)

        post_save.connect(self.signal_save, sender=Capability)
        post_save.connect(self.signal_save, sender=Property)
        post_delete.connect(self.signal_delete, sender=Capability)
        post_delete.connect(self.signal_delete, sender=Property)

    # ToDo: change topic devices
    def signal_save(self, sender, instance, *args, **kwargs):
        if instance.mqtt_config != self._config:
            return

        created = kwargs['created']
        if created:
            self.sub_topic(instance.state_topic, instance)
        else:
            if instance.state_topic not in self.topic_devices:
                topic_by_instance = self.get_topic_by_device(instance)
                if not topic_by_instance:
                    return
                self.sub_topic(instance.state_topic, instance)
                self.unsub_topic(topic_by_instance)

    def signal_delete(self, sender, instance, *args, **kwargs):
        if instance.mqtt_config != self._config:
            return

        if instance.state_topic in self.topic_devices:
            self.unsub_topic(instance.state_topic)

    def sub_topic(self, topic, device):
        print(f'\t\t\tsub {topic}')
        self.topic_devices[topic] = device
        self.client.subscribe(topic)

    def unsub_topic(self, topic):
        print(f'\t\t\tunsub {topic}')
        self.client.unsubscribe(topic)
        del self.topic_devices[topic]

    def get_topic_by_device(self, looking_for_device):
        for topic in self.topic_devices:
            device = self.topic_devices[topic]
            if device == looking_for_device:
                return topic
        return None

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc != 0:
            raise RuntimeError(f"MqttClient connected with error_code={rc}")

    def on_message(self, client, userdata, msg):
        self.handle_message(msg.topic, msg.payload.decode())

    def handle_message(self, topic, msg):
        if topic not in self.topic_devices:
            # ToDo: logging
            print("topic not in self.topic_devices")
            return
        ability = self.topic_devices[topic]

        if ability.state_topic_retriever:
            value = parse(ability.state_topic_retriever).find(json.loads(msg))[0].value
        else:
            value = msg

        if ability.type == PropertyType.FLOAT:
            ability.state[0]['value'] = float(value)
        elif ability.type == PropertyType.EVENT:
            # ToDo:
            allowed_values = ALLOWED_EVENTS_BY_EVENT_INSTANCE[ability.state[0]['instance']]
            if value in allowed_values:
                ability.state[0]['value'] = float(value)

        elif ability.type == CapabilityType.ON_OFF:
            ability.state[0]['value'] = bool(TF_TRANSLATOR[value.lower()])
        elif ability.type == CapabilityType.COLOR_SETTING:
            # ToDo: F
            pass
        elif ability.type == CapabilityType.VIDEO_STREAM:
            ability.state[0]['value']['protocols'] = value
        elif ability.type == CapabilityType.MODE:
            # ToDo:
            allowed_values = ability.modes
            if value in allowed_values:
                ability.state[0]['value'] = float(value)
        elif ability.type == CapabilityType.RANGE:
            ability.state[0]['value'] = float(value)
        elif ability.type == CapabilityType.TOGGLE:
            ability.state[0]['value'] = bool(TF_TRANSLATOR[value])

        ability.save()
        ability.update_yandex_state()

        print(f"Topic: {topic}")
        print(f"Msg: {msg}")
        print(f"Value: {value}")

    def publish_message(self, topic, payload):
        if isinstance(payload, dict):
            _payload = json.dumps(payload)
        else:
            _payload = payload
        self.client.publish(topic, _payload)
