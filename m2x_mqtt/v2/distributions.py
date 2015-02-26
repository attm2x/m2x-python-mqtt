from m2x_mqtt.v2.resource import Resource
from m2x_mqtt.v2.devices import Device


class DistributionDevice(Device):
    COLLECTION_PATH = 'distributions/{distribution_id}/devices'


class Distribution(Resource):
    COLLECTION_PATH = 'distributions'
    ITEM_PATH = 'distributions/{id}'
    ITEMS_KEY = 'distributions'

    def add_device(self, serial):
        return DistributionDevice.create(self.api, distribution_id=self.id,
                                         serial=serial)
