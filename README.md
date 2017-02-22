# AT&T's M2X MQTT Python Client

[![Documentation Status](https://readthedocs.org/projects/m2x-python-mqtt/badge/?version=latest)](http://m2x-python-mqtt.readthedocs.io/en/latest/?badge=latest)

[AT&T M2X](http://m2x.att.com) is a cloud-based fully managed time-series data storage service for network connected machine-to-machine (M2M) devices and the Internet of Things (IoT). 

The [AT&T M2X API](https://m2x.att.com/developer/documentation/overview) provides all the needed operations and methods to connect your devices to AT&T's M2X service. This library aims to provide a simple wrapper to interact with the AT&T M2X API for [Python](https://www.python.org). Refer to the [Glossary of Terms](https://m2x.att.com/developer/documentation/glossary) to understand the nomenclature used throughout this documentation.

Documentation for the AT&T M2X Python Client Library can be found [here](http://m2x-python-mqtt.readthedocs.io/en/latest/), though you should also read this README thoroughly before getting started.

Getting Started
===============

1. Signup for an [M2X Account](https://m2x.att.com/signup).
2. Obtain your _Master Key_ from the Master Keys tab of your [Account
   Settings](https://m2x.att.com/account) screen.
2. Create your first [Device](https://m2x.att.com/devices) and copy its _Device
   ID_.
3. Review the [M2X API
   Documentation](https://m2x.att.com/developer/documentation/overview).


## Description

This library provides an interface to access the MQTT API implementation with
the [AT&T's M2X service](https://m2x.att.com/), while supporting Python 2 and 3.


## Dependencies

* [iso8601](https://pypi.python.org/pypi/iso8601)
* [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt)

To use Python on your local machine, you'll need to first install
`Python-setuptools`.


## Installation

The project is very easy to install — the different options are:

```bash
$ pip install m2x-mqtt
```

or:

```bash
$ easy_install m2x-mqtt
```

or cloning the repository:

```bash
$ git clone https://github.com/attm2x/m2x-python-mqtt.git
$ cd m2x-python-mqtt
$ python setup.py install
```

## Usage

In order to communicate with the M2X API, you need an instance of
[M2XClient](m2x_mqtt/client.py). You need to pass your API key in the
constructor to access your data.

```python
from m2x_mqtt.client import M2XClient

client = M2XClient(key='<API-KEY>')
```

This `client` an interface to your data in M2X

- [Distributions](m2x/v2/distributions.py)
  ```python
  distribution = client.distribution('<DISTRIBUTION-ID>')
  ```

- [Devices](m2x/v2/devices.py)
  ```python
  device = client.device('<DEVICE-ID>')
  ```

## Example

Here's an example of a simple application that will load the current time to
a stream every 10 seconds:

```python
import os
import time

from m2x_mqtt.client import M2XClient


# Instantiate a client
client = M2XClient(key=os.environ['API_KEY'])

# Create a device
device = client.create_device(
    name='Current Time Example',
    description='Store current time every 10 seconds',
    visibility='public'
)

# Create a data stream
stream = device.create_stream('current_time')

# And now register the current time every 10 seconds (hit ctrl-c to kill)
while True:
    stream.add_value(int(time.time()))
    time.sleep(10)
```

To run this example you need a `API Key` and execute it like this:

```bash
$ API_KEY=<API-KEY-TOKEN> python ./example.py
```

## Versioning

This lib aims to adhere to [Semantic Versioning 2.0.0](http://semver.org/). As
a summary, given a version number `MAJOR.MINOR.PATCH`:

1. `MAJOR` will increment when backwards-incompatible changes are introduced to
   the client.
2. `MINOR` will increment when backwards-compatible functionality is added.
3. `PATCH` will increment with backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as
extensions to the `MAJOR.MINOR.PATCH` format.

**Note**: the client version does not necessarily reflect the version used in
          the AT&T M2X API.

## License

This library is released under the MIT license. See [LICENSE](LICENSE) for the terms.
