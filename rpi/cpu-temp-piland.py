############################################################
# Simple Python program that repeatedly reads the
# Raspberry Pi's internal CPU temperature sensor and 
# writes the current value to Pi Land. 
#
# To run this program from the bash command prompt,
# type this and hit Enter:
#
#    python cpu-temp-piland.py
#
############################################################

import time
import requests

# Write the value to a specific data slot in a Pi Land room

# NOTE:  Change the room, dataslot, and devicename below to something
#        different for your own use so that everyone isn't using
#        the same data slot and overwriting each other's data.

# Pi Land settings
room = 404                             # Room number to use (1 through 999)
slot = 1                               # Data slot number to use (1 through 30)
name = "Pi+CPU+Temp"                   # Descriptive name for your device, put '+' for space char

# Sensor settings
devicepath = open("/sys/class/thermal/thermal_zone0/temp")

# Other global variables
baseurl = "http://piland.socialdevices.io"
baseurl = baseurl + "/" + str(room) + "/write/" + str(slot) + "?name=" + name + "&value="

while True:
  
  # Read the temperature value

  devicepath.seek(0,0);
  rawtemp = devicepath.read().rstrip()

  # Convert to the units we want

  tempC = float(rawtemp) / 1000.0
  tempF = (tempC * 1.8) + 32

  url = baseurl + "%0.3f" % tempC + "+C"

  print url

  requests.get(url)    # write data

  time.sleep(2.0)      # 2 second delay

