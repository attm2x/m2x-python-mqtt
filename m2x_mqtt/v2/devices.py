from m2x_mqtt.v2.resource import Resource
from m2x_mqtt.v2.streams import Stream
from m2x_mqtt.v2.commands import Command


class Device(Resource):
    """ Wrapper for AT&T M2X `Device API <https://m2x.att.com/developer/documentation/v2/device>`_
    """
    COLLECTION_PATH = 'devices'
    ITEM_PATH = 'devices/{id}'
    ITEMS_KEY = 'devices'

    def stream(self, name):
        """ Method for `View Data Stream <https://m2x.att.com/developer/documentation/v2/device#View-Data-Stream>`_ endpoint.

        :param name: The name of the Stream being retrieved

        :return: The matching Stream
        :rtype: Stream
        """
        return Stream(self.api, self, name=name)

    def create_stream(self, name, **params):
        """ Method for `Create/Update Data Stream <https://m2x.att.com/developer/documentation/v2/device#Create-Update-Data-Stream>`_ endpoint.

        :param name: Name of the stream to be created
        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: The newly created Stream
        :rtype: Stream
        """
        return Stream.create(self.api, self, name, **params)

    def post_updates(self, **values):
        """ Method for `Post Device Updates (Multiple Values to Multiple Streams) <https://m2x.att.com/developer/documentation/v2/device#Post-Device-Updates--Multiple-Values-to-Multiple-Streams->`_ endpoint.

        :param values: The values being posted, formatted according to the API docs
        :type values: dict

        :return: The API response, see M2X API docs for details
        :rtype: dict
        """
        return self.api.post(self.subpath('/updates'), data=values)

    def update_location(self, **params):
        """ Method for `Update Device Location <https://m2x.att.com/developer/documentation/v2/device#Update-Device-Location>`_ endpoint.

        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: The API response, see M2X API docs for details
        :rtype: dict
        """
        return self.api.put(self.subpath('/location'), data=params)

    def command(self, id):
        """ Method for `View Command Details <https://m2x.att.com/developer/documentation/v2/commands#View-Command-Details>`_ endpoint.

        :param id: ID of the Command to retrieve
        :type id: str

        :return: The matching Command
        :rtype: Command
        """
        return Command(self.api, self, id=id)

    def commands(self, **params):
        """ Method for `List Sent Commands <https://m2x.att.com/developer/documentation/v2/commands#List-Sent-Commands>`_ endpoint.

        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: List of :class:`.Command` objects
        :rtype: `list <https://docs.python.org/2/library/functions.html#list>`_
        """
        res = self.api.get(self.subpath('/commands'), data=params)
        return (Command(self.api, self, **data) for data in res[Command.ITEMS_KEY])

    def post_device_update(self, **params):
        """ Method for `Post Device Updates (Multiple Values to Multiple Streams) <https://m2x.att.com/developer/documentation/v2/device#Post-Device-Updates--Multiple-Values-to-Multiple-Streams->`_ endpoint.

        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: The API response, see M2X API docs for details
        :rtype: dict
        """
        return self.api.post(self.subpath('/update'), **params)

    @classmethod
    def search(cls, api, **params):
        response = api.post('devices/search', **params)
        return cls.itemize(api, response)
