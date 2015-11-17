from m2x_mqtt.v2.resource import Resource


class Command(Resource):
    COLLECTION_PATH = 'devices/{device_id}/commands'
    ITEM_PATH = 'devices/{device_id}/commands/{id}'
    ITEMS_KEY = 'commands'

    def __init__(self, api, device, **data):
        self.device = device
        super(Command, self).__init__(api, **data)

    def subpath(self, path):
        return self.item_path(self.id, device_id=self.device.id) + path

    def process(self, **response_data):
        return self.api.post(self.subpath('/process'), data=response_data)

    def reject(self, **response_data):
        return self.api.post(self.subpath('/reject'), data=response_data)
