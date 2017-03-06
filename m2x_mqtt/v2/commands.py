from m2x_mqtt.v2.resource import Resource

class Command(Resource):
    """ Wrapper for AT&T M2X `Commands API <https://m2x.att.com/developer/documentation/v2/commands>`_
    """
    COLLECTION_PATH = 'devices/{device_id}/commands'
    ITEM_PATH = 'devices/{device_id}/commands/{id}'
    ITEMS_KEY = 'commands'

    def __init__(self, api, device, **data):
        self.device = device
        super(Command, self).__init__(api, **data)

    def subpath(self, path):
        return self.item_path(self.id, device_id=self.device.id) + path

    def process(self, **response_data):
        """ Method for `Device Marks a Command as Processed <https://m2x.att.com/developer/documentation/v2/commands#Device-Marks-a-Command-as-Processed>`_ endpoint.

        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: The API response, see M2X API docs for details
        :rtype: dict
        """
        return self.api.post(self.subpath('/process'), data=response_data)

    def reject(self, **response_data):
        """ Method for `Device Marks a Command as Rejected <https://m2x.att.com/developer/documentation/v2/commands#Device-Marks-a-Command-as-Rejected>`_ endpoint.

        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: The API response, see M2X API docs for details
        :rtype: dict
        """
        return self.api.post(self.subpath('/reject'), data=response_data)
