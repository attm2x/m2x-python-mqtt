import os
from m2x_mqtt.client import M2XClient

"""
This example demonstrates how to update single values to multiple streams to target device

API Documentation:
https://m2x.att.com/developer/documentation/v2/device#Post-Device-Update--Single-Values-to-Multiple-Streams-
"""

API_KEY = os.environ['API_KEY']
DEVICE  = os.environ['DEVICE']

client = M2XClient(key=API_KEY)
device = client.device(DEVICE)

params = {
    "timestamp" : "<YOUR-TIME-IN-ISO-8601-FORMAT>",
    "values" : {
        "<YOUR-EXISTING-STREAM-NAME>": "<YOUR-NEW-STREAM-VALUE>",
        "<YOUR-EXISTING-STREAM-NAME>" : "<YOUR-NEW-STREAM-VALUE>"
    }
}

response = device.post_device_update(data = params)
print("Response: %s" % response)
