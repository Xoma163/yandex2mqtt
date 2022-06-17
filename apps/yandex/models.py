from typing import List

# from django.db import models

from apps.yandex.capabilities.Capability import Capability
from apps.yandex.devices.Device import Device as DeviceType
from apps.yandex.properties.Property import Property


class Room:
    def __init__(self, name):
        self.name = name


class Device:
    def __init__(
            self,
            pk: int,
            _type: DeviceType,
            name: str,

            room: Room = None,
            description: str = None,
            custom_data: dict = None,
            capabilities: List[Capability] = None,
            properties: List[Property] = None
    ):

        if not isinstance(pk, int):
            raise RuntimeError("pk must be int instance")

        self.pk: int = pk

        if not isinstance(name, str):
            raise RuntimeError("name must be str instance")

        self.name: str = name

        if not isinstance(_type, DeviceType):
            raise RuntimeError("_type must be DeviceType instance")

        self.type: str = _type.value

        if room:
            if not isinstance(room, Room):
                raise RuntimeError("room must be Room instance")
        self.room: Room = room

        if room:
            if not isinstance(description, str):
                raise RuntimeError("description must be str instance")
        self.description: str = description

        if custom_data:
            if not isinstance(custom_data, dict):
                raise RuntimeError("custom_data must be dict instance")
        self.custom_data: dict = custom_data

        if not capabilities and not properties:
            raise RuntimeError("capabilities or properties must be provided")

        if capabilities:
            if not isinstance(capabilities, list):
                raise RuntimeError("capabilities must be list instance")
            for capability in capabilities:
                if not isinstance(capability, Capability):
                    raise RuntimeError("capability must be Capability instance")
        else:
            capabilities = []
        self.capabilities: List[Capability] = capabilities

        if properties:
            if not isinstance(properties, list):
                raise RuntimeError("properties must be list instance")
            for _property in properties:
                if not isinstance(_property, Property):
                    raise RuntimeError("properties must be Property instance")
        else:
            properties = []
        self.properties: List[Property] = properties

    def get_json(self):
        data = {
            "id": self.pk,
            "name": self.name,
            "type": self.type,
        }
        if self.room:
            data["room"] = self.room.name

        if self.description:
            data["description"] = self.description
        if self.custom_data:
            data["custom_data"] = self.custom_data
        if self.capabilities:
            data["capabilities"] = [x.get_json() for x in self.capabilities]
        if self.properties:
            data["properties"] = [x.get_json() for x in self.properties]

        return data
