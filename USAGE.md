# AT&T's M2X MQTT Python Client - Usage

To create a client instance only a single parameter, the API Key, is needed.
Your API Keys can be found in your account settings. To create a client
instance just do:

```python
>>> from m2x_mqtt.client import M2XClient
>>> client = M2XClient(key='YOUR API KEY HERE')
```

The client provides an interface to:
    * Create devices (and update location)
    * Create streams
    * Create values


## Devices

#### Creation:

```python
>>> device = client.create_device(
...     name='Devices',
...     description='Device description',
...     visibility='public'
... )
<m2x_mqtt.v2.devices.Device at 0x365c590>
```

#### Update a location:

```python
>>> device.update_location(
    elevation=5,
    latitude=-37.9788423562422,
    longitude=-57.5478776916862,
    name='Storage Room',
    timestamp='2014-09-10T19:15:00.756Z'
)
{'status': 'accepted'}
```

#### Device updates (post several values to the device in a single request):

```python
>>> from datetime import datetime
>>> device.post_updates(values={
    'stream1': [
        {
            'timestamp': datetime.now(),
            'value': 100
        }, {
            'timestamp': datetime.now(),
            'value': 200
        }
    ],
    'stream2': [
        {
            'timestamp': datetime.now(),
            'value': 300
        }, {
            'timestamp': '2015-02-03T00:33:43.422440Z'
            'value': 400
        }
    ]
})
```

## Streams

`Streams` can be seen as collection of values, M2X provides some useful
methods for streams.

#### Values

```python
>>> from datetime import datetime
>>> stream = device.stream(name='...')
<m2x_mqtt.v2.streams.Stream at 0x7f6791d12290>
>>> stream.add_value(123)
{'status': 'accepted'}
>>> stream.post_values([{
    'value': 123, 'timestamp': datetime.now()
}, {
    'value': 456, 'timestamp': datetime.now()
})
{'status': 'accepted'}
```

## Distributions

`Devices` can be grouped by `Distributions`. It's provided here as a mean to
create devices in a distribution.

#### Create a device

```python
>>> distribution = client.distribution(...)
<m2x_mqtt.v2.distributions.Distribution at 0x7f6791d12290>
>>> distribution.add_device(name='Device name', visibility='public')
<m2x_mqtt.v2.devices.Device at 0x365c590>
```

## Lets build a RandomNumberGenerator Data Source

Lets build a python random number generator data source using the API
described above.

```python
# First import everything:
import random
from m2x_mqtt.client import M2XClient

# Create a client instance:
client = M2XClient(key='288b375565d3402a8b6bd8c343e9fcad')

# Now create a device for the values:
device = client.create_device(
    name='RNG Device Example',
    description='Device for RandomNumberGenerator example',
    visibility='public'
)

# Create a data stream in the feed:
stream = device.create_stream(name='values')

# And now it's time to register some values in the stream:
for x in range(10):
    stream.add_value(random.randint(0, 100))

# Lets print the values:
for val in stream.values():
    print '{0} - {1}'.format(val.at.strftime('%Y-%m-%d %H:%M:%S'),
                             val.value)
```
