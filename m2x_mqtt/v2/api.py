from m2x_mqtt.api import MQTTAPIBase
from m2x_mqtt.v2.devices import Device
from m2x_mqtt.v2.distributions import Distribution


class MQTTAPIVersion2(MQTTAPIBase):
    """ Wrapper for `AT&T M2X API <https://m2x.att.com/developer/documentation/v2/overview>`_
    """
    PATH = '/v2'

    def device(self, id):
        """ Method for `View Device Details <https://m2x.att.com/developer/documentation/v2/device#View-Device-Details>`_ endpoint.

        :param id: ID of the Device to retrieve
        :type id: str

        :return: The matching Device
        :rtype: Device
        """
        return Device(self, id=id)

    def create_device(self, **params):
        """ Method for `Create Device <https://m2x.att.com/developer/documentation/v2/device#Create-Device>`_ endpoint.

        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: The newly created Device
        :rtype: Device
        """
        return Device.create(self, **params)

    def distribution(self, id):
        """ Method for `View Distribution Details <https://m2x.att.com/developer/documentation/v2/distribution#View-Distribution-Details>`_ endpoint.

        :param id: ID of the Distribution to retrieve
        :type id: str

        :return: The matching Distribution
        :rtype: Distribution
        """
        return Distribution(self, id=id)

    def devices(self, **params):
        """ Method for `List Devices <https://m2x.att.com/developer/documentation/v2/device#List-Devices>`_ endpoint.

        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: List of :class:`.Device` objects
        :rtype: `list <https://docs.python.org/2/library/functions.html#list>`_
        """
        return Device.list(self, **params)
