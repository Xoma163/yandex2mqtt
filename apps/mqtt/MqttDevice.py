from apps.mqtt.MqttClient import MqttClient


class MqttDevice:
    ON = 1
    OFF = 0

    def __init__(self, mqtt_client: MqttClient, control_topic: str = None, state_topic: str = None):
        self.mqtt_client = mqtt_client

        if not isinstance(mqtt_client, MqttClient):
            raise RuntimeError("mqtt_client must be MqttClient instance")

        if not control_topic and not state_topic:
            raise RuntimeError("control_topic or state_topic must be provided")

        if control_topic:
            if not isinstance(control_topic, str):
                raise RuntimeError("control_topic must be str instance")
        if state_topic:
            if not isinstance(state_topic, str):
                raise RuntimeError("state_topic must be str instance")

        self.control_topic = control_topic
        self.state_topic = state_topic

    def send_to_control_topic(self, payload):
        self.mqtt_client.publish_message(self.control_topic, payload)

    # def get_state_by_val(self):
    #     """
    #     Получение состояние устройства по строке
    #     """
