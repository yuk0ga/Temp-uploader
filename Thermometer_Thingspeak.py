#!/usr/bin/env python
# Joshwa
# This code plots the temperature vs time graph online using thingspeak measured by a thermometer.
# The Thermometer value is read by BrickPi mounted on RaspberryPi.
# For more information on BrickPi and Thermometer sensor visit http://www.dexterindustries.com/
# To get started on basics of pushing data to thingspeak visit : www.australianrobotics.com.au/news/how-to-talk-to-thingspeak-with-python-a-memory-cpu-monitor
# For the working of thermometer code alone visit : https://github.com/DexterInd/BrickPi/blob/master/Software/BrickPi_Python/Sensor%20Examples/DI-dTemp%20test.py
# Connect the Thermometer to the SENSOR PORT_3 of BrickPi

import httplib, urllib
import time
import subprocess
import math

def thermometer():
  while True :
    output =  subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
    # extract temperature from output
    temp = output[5:9]
    params = urllib.urlencode({'field1': temp, 'key':'GF3ZF52RXEJM97WL'})     # use your API key generated in the thingspeak channels for the value of 'key'
    # temp is the data you will be sending to the thingspeak channel for plotting the graph. You can add more than one channel and plot more graphs
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
      conn.request("POST", "/update", params, headers)
      response = conn.getresponse()
      print temp
      print response.status, response.reason
      data = response.read()
      conn.close()
    except:
      print "connection failed"
    break
#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
    while True:
      thermometer()
      time.sleep(16)
