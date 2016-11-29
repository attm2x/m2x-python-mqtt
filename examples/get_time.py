import os
from m2x_mqtt.client import M2XClient
from m2x_mqtt.v2.time import Time

"""
This example demonstrates how to get server's time from target device

API Documentation:
https://m2x.att.com/developer/documentation/v2/time
"""

API_KEY = os.environ['API_KEY']

# Instantiate a client
client = M2XClient(key=API_KEY)

# Instantiate time for the client
time = Time(client)

# Getting the Time in various formats
print("Server time in ISO8601 format: " + time.get_time_in_iso8601())
print("Server time in seconds: " + time.get_time_in_seconds())
print("Server time in milliseconds: " + time.get_time_in_millis())
