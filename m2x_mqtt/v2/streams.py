from m2x_mqtt.v2.resource import Resource


class Stream(Resource):
    ITEM_PATH = 'devices/{device_id}/streams/{name}'
    COLLECTION_PATH = 'devices/{device_id}/streams'
    ITEMS_KEY = 'streams'
    ID_KEY = 'name'

    def __init__(self, api, device, **data):
        self.device = device
        super(Stream, self).__init__(api, **data)

    def add_value(self, value, timestamp=None):
        data = {'value': value}
        if timestamp:
            data['timestamp'] = timestamp
        return self.api.put(self.subpath('/value'), data=data)

    update_value = add_value

    def post_values(self, values):
        return self.api.post(self.subpath('/values'), data={
            'values': values
        })

    def subpath(self, path):
        return self.item_path(self.name, device_id=self.device.id) + path

    @classmethod
    def create(cls, api, device, name, **attrs):
        path = cls.item_path(name, device_id=device.id)
        params = cls.to_server(attrs)
        path = path or cls.item_path(name, **params)
        response = api.put(path, data=params)
        response = cls.from_server(response or params)
        return cls.item(api, response, device=device)
