import os
import subprocess
import time
from m2x_mqtt.client import M2XClient

##
# This example demonstrates a basic command-driven application.
#
# It has a method called process_commands that executes and the given command.
# Each command is acknowledged by either the #process! or #reject! method.
#
# This example application supports three basic commands:
#   SAY    - print the message given in the command data field "message".
#   REPORT - respond with a report containing the public IP and process ID.
#
# Upon startup, it queries the M2X API to check for any outstanding
# unacknowledged commands for the current device and processes them.
# After that, it enters a loop of processing each new command as it arrives
# via command delivery notifications. A more robust application would also
# periodically query the M2X API to check for outstanding commands again,
# as it is possible to miss delivery notifications in a network partition.

API_KEY = os.environ['API_KEY']
DEVICE  = os.environ['DEVICE']

ALLOWED_COMMANDS = ['SAY', 'REPORT']

def process_command(command):
    name = command['name'].upper()

    if   name == 'SAY':    process_say_command(command)
    elif name == 'REPORT': process_report_command(command)
    else:
        reason = 'unknown command name; allowed names are: ' + str(ALLOWED_COMMANDS)
        command.reject(reason=reason)

def process_say_command(command):
    try:
        message = command['data']['message']
    except KeyError:
        command.reject(reason='"message" data is required')
        return

    print("SAY: " + message)

    command.process()

def process_report_command(command):
    ip = subprocess.check_output("curl -s ifconfig.co", shell=True).strip()
    pid = str(os.getpid())
    report = { 'public_ip': ip, 'pid': pid }

    print("REPORT: " + str(report))

    command.process(**report)

def process_unacknowledged_commands(device):
    for command in device.commands(status='pending', order='asc'):
        command.refresh()
        process_command(command)

def process_received_commands(client):
    for command in client.receive_commands():
        process_command(command)


# Create a client instance using a primary device API key.
# The keepalive parameter can be raised for low-bandwidth applications.
client = M2XClient(key=API_KEY, keepalive=60)

# Access the correspending device by ID
device = client.device(DEVICE)

# Process unacknowledged commands on startup
process_unacknowledged_commands(device)

# Process received commands in an infinite loop
while True:
    process_received_commands(client)
    time.sleep(1)
