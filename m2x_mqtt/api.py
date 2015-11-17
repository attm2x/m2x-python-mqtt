import json
import uuid
import time
import threading

from paho.mqtt.client import MQTT_ERR_SUCCESS, Client as MQTTClient

from m2x_mqtt.utils import DateTimeJSONEncoder
from m2x_mqtt.v2.devices import Device
from m2x_mqtt.v2.commands import Command


class MQTTResponse(object):
    def __init__(self, response):
        self.response = response
        self.raw = response
        self.status = response['status']
        self.headers = {}
        self.json = response

    @property
    def success(self):
        return self.status >= 200 and self.status < 300

    @property
    def client_error(self):
        return self.status >= 400 and self.status < 500

    @property
    def server_error(self):
        return self.status >= 500

    @property
    def error(self):
        return self.client_error or self.server_error


class MQTTAPIBase(object):
    PATH = '/'

    def __init__(self, key, client, timeout=600, **kwargs):
        self.timeout = timeout
        self.apikey = key
        self.client = client
        self._locals = threading.local()

    def get(self, path, **kwargs):
        return self.request(path, method='GET', **kwargs)

    def post(self, path, **kwargs):
        return self.request(path, method='POST', **kwargs)

    def put(self, path, **kwargs):
        return self.request(path, method='PUT', **kwargs)

    @property
    def last_response(self):
        return getattr(self._locals, 'last_response', None)

    @last_response.setter
    def last_response(self, value):
        self._locals.last_response = value

    def to_json(self, value):
        return json.dumps(value, cls=DateTimeJSONEncoder)

    @property
    def mqtt(self):
        if not hasattr(self, '_mqtt_client'):
            self.responses = {}
            self._commands = []
            self.ready = False
            client = MQTTClient()
            client.username_pw_set(self.apikey)
            client.on_connect = self._on_connect
            client.on_message = self._on_message
            client.on_subscribe = self._on_subscribe
            client.connect(self.client.endpoint.replace('mqtt://', ''))
            self._mqtt_client = client
            # Start the loop and wait for the connection to be ready
            self._mqtt_client.loop_start()
            while not self.ready:
                time.sleep(.1)
        return self._mqtt_client

    def _on_connect(self, client, userdata, flags, rc):
        self._responses_topic = 'm2x/{apikey}/responses'.format(apikey=self.apikey)
        self._commands_topic = 'm2x/{apikey}/commands'.format(apikey=self.apikey)
        client.subscribe(self._responses_topic)
        client.subscribe(self._commands_topic)

    def _on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload)

        if topic == self._responses_topic:
            self.responses[payload['id']] = payload
        elif topic == self._commands_topic:
            self._commands.append(payload)

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        self.ready = True

    def url(self, *parts):
        parts = (self.PATH,) + parts
        return '/{0}'.format('/'.join(map(lambda p: p.strip('/'),
                                          filter(None, parts))))

    def receive_commands(self):
        while self._commands:
            data = self._commands.pop(0)
            device = Device(self, id=data['url'].split("/")[-3])
            yield Command(self, device, **data)

    def wait_for_response(self, msg_id):
        timeout = self.timeout

        while msg_id not in self.responses:
            time.sleep(.1)
            if timeout is not None:
                if timeout > 0:
                    timeout -= 1
                else:
                    break
        if msg_id in self.responses:
            response = self.responses.pop(msg_id)
            self.last_response = MQTTResponse(response)
            if 'body' in response:
                response = response['body']
            return response

    def request(self, path, apikey=None, method='GET', **kwargs):
        msg_id = uuid.uuid4().hex
        msg = self.to_json({
            'id': msg_id,
            'method': method,
            'resource': self.url(path),
            'body': kwargs.get('data') or kwargs.get('params') or {}
        })
        status, mid = self.mqtt.publish('m2x/{apikey}/requests'.format(
            apikey=apikey or self.apikey
        ), payload=msg)
        if status == MQTT_ERR_SUCCESS:
            return self.wait_for_response(msg_id)
