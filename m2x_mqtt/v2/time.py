from m2x_mqtt.v2.resource import Resource


class Time(Resource):
    COLLECTION_PATH = 'time'
    FORMAT_SECONDS = "time/seconds"
    FORMAT_MILLIS = "time/millis"
    FORMAT_ISO8601 = "time/iso8601"

    def __init__(self, api):
        super(Time, self).__init__(api)

    def get_time(self):
        return self.api.get(self.COLLECTION_PATH)

    def get_time_in_millis(self):
        return self.api.get(self.FORMAT_MILLIS)

    def get_time_in_seconds(self):
        return self.api.get(self.FORMAT_SECONDS)

    def get_time_in_iso8601(self):
        return self.api.get(self.FORMAT_ISO8601)