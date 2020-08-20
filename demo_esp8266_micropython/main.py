
"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your


projects by simply dragging and dropping widgets.

  Downloads, docs, tutorials: http://www.blynk.cc
  Sketch generator:           http://examples.blynk.cc
  Blynk community:            http://community.blynk.cc

  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app

This example shows how to initialize your ESP8266/ESP32 board
and connect it to Blynk.
Don't forget to change WIFI_SSID, WIFI_PASS and BLYNK_AUTH ;)
"""

import BlynkLib
import network
import machine
import time


WIFI_SSID = 'ITGenius_2G'  # SAMIT_P30
WIFI_PASS = 'it377040'  # smk377040
# Npd2V1f4WLq1-tgWKBYR_bnqGF5Yh92b
BLYNK_AUTH = '2_USzRXNq1ZMimvQslFH9J3bqaNeHXRG'
BLYNK_SERVER = 'blynk.observies.com'
BLYNK_PORT = 8080


print("Connecting to WiFi...")


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)


while not wifi.isconnected():
    pass


print('IP:', wifi.ifconfig()[0])
print("Connecting to Blynk...")


# blynk = BlynkLib.Blynk(BLYNK_AUTH)
blynk = BlynkLib.Blynk(BLYNK_AUTH, server=BLYNK_SERVER,
                       port=BLYNK_PORT, heartbeat=30)


@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')


def runLoop():
    while True:
        blynk.run()
        machine.idle()


led = machine.Pin(2, machine.Pin.OUT)
ledD5 = machine.Pin(14, machine.Pin.OUT)

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value))
    if value == ['1']:
        led.value(1)
    else:
        led.value(0)


@blynk.VIRTUAL_WRITE(5)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value))
    if value == ['1']:
        ledD5.value(1)
    else:
        ledD5.value(0)


@blynk.VIRTUAL_READ(2)
def my_read_handler():
    # this widget will show some time in seconds..
    blynk.virtual_write(2, int(time.time()))

# Run blynk in the main thread:


runLoop()

# Or, run blynk in a separate thread (unavailable for esp8266):
#import _thread
# _thread.stack_size(5*1024)
#_thread.start_new_thread(runLoop, ())

# Note:
# Threads are currently unavailable on some devices like esp8266
# ESP32_psRAM_LoBo has a bit different thread API:
# _thread.start_new_thread("Blynk", runLoop, ())
