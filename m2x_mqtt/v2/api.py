from m2x_mqtt.api import MQTTAPIBase
from m2x_mqtt.v2.devices import Device
from m2x_mqtt.v2.distributions import Distribution


class MQTTAPIVersion2(MQTTAPIBase):
    PATH = '/v2'

    def device(self, id):
        return Device(self, id=id)

    def create_device(self, **params):
        return Device.create(self, **params)

    def distribution(self, id):
        return Distribution(self, id=id)
