# Usage:
#   $ API_KEY=<YOUR MASTER API KEY> python example.py

import os
from m2x_mqtt.client import M2XClient
from m2x_mqtt.v2.devices import Device

"""
This example demonstrates how to search for devices.
API Documentation:
https://m2x.att.com/developer/documentation/v2/device#Search-Devices
"""

API_KEY = os.environ['API_KEY']

# Instantiate a client
client = M2XClient(key=API_KEY)

params = {
    "visibility": "private",
    "status": "enabled",
    "limit": "6"
}

devices = Device.search(api = client, params = params)

if len(devices) > 0:
    print("\nDevice Details :")
    for device in devices:
        print("Device name: %s Device Id: %s Device Visibility: %s Device Status: %s " % (device.name, device.id, device.visibility, device.status ))
else:
    print("Devices not available in this search criteria")
