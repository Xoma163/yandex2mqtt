from apps.yandex.capabilities.CapabilityUtils.Status import Status


class Capability:
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/capability-types.html
    """

    def __init__(self, **kwargs):
        self.type = None
        self.parameters = {}
        self.retrievable = kwargs.get('retrievable', True) # Признак включенного оповещения об изменении состояния умения при помощи сервиса уведомлений
        self.reportable = kwargs.get('reportable', False) # Доступен ли для данного умения устройства запрос состояния
        self.value = kwargs.get('value', False) # Изначальное значение

    def get_for_device_list(self):
        return {
            'type': self.type,
            'retrievable': self.retrievable,
            'reportable': self.reportable,
            'parameters': self.parameters,
        }

    def get_state(self):
        return {
            "type": self.type,
            "state": {
                "instance": "on",
                "value": self.value,
            }
        }

    def switch_state(self, new_value):
        # ToDo: switch with new_value
        error = None
        try:
            self.value = new_value
        except Exception as e:
            error = f"Ошибка какая-то\n{str(e)}"

        data = {
            "type": self.type,
            "state": {
                "instance": "on"
            }
        }
        if not error:
            data['state']['action_result'] = {
                "status": Status.DONE.value,
            }
        else:
            data['state']["action_result"] = {
                "status": Status.ERROR.value,
                "error_message": error
            }

        return data
