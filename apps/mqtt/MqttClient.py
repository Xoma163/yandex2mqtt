import logging

import paho.mqtt.client as mqtt
import json

from django.db.models.signals import post_save, post_delete

from apps.yandex.consts import PropertyType, ALLOWED_EVENTS_BY_EVENT_INSTANCE, CapabilityType, TF_TRANSLATOR
from jsonpath_ng import parse

from apps.mqtt.models import MqttConfig
from apps.yandex.models import Capability, Property

logger = logging.getLogger("mqtt")


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
        logger.info(f"Старт вечного слушателя mqtt для конфига {self._config}")
        self.client.loop_forever()

    def subscribe(self):
        self.sub_and_add_signals(Capability)
        self.sub_and_add_signals(Property)

    def sub_and_add_signals(self, model):
        for obj in model.objects.filter(mqtt_config=self._config):
            self.sub_topic(obj.state_topic, obj)
        post_save.connect(self.signal_save, sender=model)
        post_delete.connect(self.signal_delete, sender=model)

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
        logger.info(f"Подписались на топик \"{topic}\"")
        self.topic_devices[topic] = device
        self.client.subscribe(topic)

    def unsub_topic(self, topic):
        logger.info(f"Отписались от топика \"{topic}\"")
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
            logger.error("Ошибка подключения к mqtt")
            raise RuntimeError(f"MqttClient connected with error_code={rc}")
        logger.info("Успешно подключено к mqtt")

    def on_message(self, client, userdata, msg):
        try:
            self.handle_message(msg.topic, msg.payload.decode())
        except Exception as e:
            logger.exception("Ошибка в on_message")

    def handle_message(self, topic, msg):
        if topic not in self.topic_devices:
            logger.error(f"topic {topic}" "not in self.topic_devices")
            return
        ability = self.topic_devices[topic]

        if ability.state_topic_retriever:
            value = parse(ability.state_topic_retriever).find(json.loads(msg))[0].value
        else:
            value = msg
        data = {"topic": topic, "msg": msg, "value": value, "ability": str(ability)}
        logger.debug(f"Получено сообщение mqtt: {data}")

        if ability.type == PropertyType.FLOAT.value:
            ability.state[0]['value'] = float(value)
        elif ability.type == PropertyType.EVENT.value:
            # ToDo:
            allowed_values = ALLOWED_EVENTS_BY_EVENT_INSTANCE[ability.state[0]['instance']]
            if value in allowed_values:
                ability.state[0]['value'] = float(value)

        elif ability.type == CapabilityType.ON_OFF.value:
            ability.state[0]['value'] = bool(TF_TRANSLATOR[value.lower()])
        elif ability.type == CapabilityType.COLOR_SETTING.value:
            # ToDo: F
            pass
        elif ability.type == CapabilityType.VIDEO_STREAM.value:
            ability.state[0]['value']['protocols'] = value
        elif ability.type == CapabilityType.MODE.value:
            # ToDo:
            allowed_values = ability.modes
            if value in allowed_values:
                ability.state[0]['value'] = float(value)
        elif ability.type == CapabilityType.RANGE.value:
            ability.state[0]['value'] = float(value)
        elif ability.type == CapabilityType.TOGGLE.value:
            ability.state[0]['value'] = bool(TF_TRANSLATOR[value])

        ability.save()
        ability.update_yandex_state()

    def publish_message(self, topic, payload):
        logger.info(f"Отправляем сообщение в топик \"{topic}\", сообщение \"{payload}\"")
        if isinstance(payload, dict):
            _payload = json.dumps(payload)
        else:
            _payload = payload
        self.client.publish(topic, _payload)
