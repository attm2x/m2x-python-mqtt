from m2x_mqtt.v2.resource import Resource
from m2x_mqtt.v2.devices import Device


class DistributionDevice(Device):
    COLLECTION_PATH = 'distributions/{distribution_id}/devices'


class Distribution(Resource):
    """ Wrapper for AT&T M2X `Distribution API <https://m2x.att.com/developer/documentation/v2/distribution>`_
    """
    COLLECTION_PATH = 'distributions'
    ITEM_PATH = 'distributions/{id}'
    ITEMS_KEY = 'distributions'

    def add_device(self, serial):
        """ Method for `Add Device to an Existing Distribution <https://m2x.att.com/developer/documentation/v2/distribution#Add-Device-to-an-existing-Distribution>`_ endpoint.

        :param serial: The unique (account-wide) serial for the DistributionDevice being added to the Distribution

        :return: The newly created DistributionDevice
        :rtype: DistributionDevice

        :raises: :class:`~requests.exceptions.HTTPError` if an error occurs when sending the HTTP request
        """
        return DistributionDevice.create(self.api, distribution_id=self.id,
                                         serial=serial)
