# Usage:
#   $ API_KEY=<YOUR MASTER API KEY> python example.py

import os
from m2x_mqtt.client import M2XClient

"""
This example demonstrates how to get a paginated list of devices.
API Documentation:
https://m2x.att.com/developer/documentation/v2/device#List-Devices
"""

API_KEY = os.environ['API_KEY']

# Instantiate a client
client = M2XClient(key=API_KEY)

# Make an initial call to List Devices
# to get the first page & number of pages
limit = 2
page_of_devices = client.devices(limit=limit)
number_of_pages = client.last_response.response['body']['pages']
total_devices = client.last_response.response['body']['total']

print("Total Number of Devices: {t}".format(t=total_devices))

# Iterate over all pages of devices
for page in range(1, number_of_pages + 1):
    print("{d} devices returned on page {p}".format(d=len(page_of_devices),p=page))
    next_page = page + 1
    page_of_devices = client.devices(page=next_page, limit=limit)
