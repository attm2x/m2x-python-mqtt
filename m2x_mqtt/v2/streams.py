from m2x_mqtt.v2.resource import Resource


class Stream(Resource):
    """ Methods for interacting AT&T M2X Device Streams
    """
    ITEM_PATH = 'devices/{device_id}/streams/{name}'
    COLLECTION_PATH = 'devices/{device_id}/streams'
    ITEMS_KEY = 'streams'
    ID_KEY = 'name'

    def __init__(self, api, device, **data):
        self.device = device
        super(Stream, self).__init__(api, **data)

    def add_value(self, value, timestamp=None):
        """ Method for `Update Data Stream Value <https://m2x.att.com/developer/documentation/v2/device#Update-Data-Stream-Value>`_ endpoint.

        :param value: The updated stream value
        :param timestamp: The (optional) timestamp for the upadted value

        :return: The API response, see M2X API docs for details
        :rtype: dict
        """
        data = {'value': value}
        if timestamp:
            data['timestamp'] = timestamp
        return self.api.put(self.subpath('/value'), data=data)

    update_value = add_value

    def post_values(self, values):
        """ Method for `Post Data Stream Values <https://m2x.att.com/developer/documentation/v2/device#Post-Data-Stream-Values>`_ endpoint.

        :param values: Values to post, see M2X API docs for details
        :type values: dict

        :return: The API response, see M2X API docs for details
        :rtype: dict
        """
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
