from m2x_mqtt.v2.api import MQTTAPIVersion2


class M2XClient(object):
    ENDPOINT = 'mqtt://api-m2x.att.com'

    def __init__(self, key, api=MQTTAPIVersion2, endpoint=None, **kwargs):
        self.endpoint = endpoint or self.ENDPOINT
        self.api = api(key, self, **kwargs)

    def url(self, *parts):
        return '/'.join([part.strip('/') for part in (self.endpoint,) + parts
                            if part])

    def __getattr__(self, name):
        return getattr(self.api, name)
