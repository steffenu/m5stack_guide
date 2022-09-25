from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(15)


# DISPLAY CURRENT REDMINE TASKS on SCREEN
# -> subject, done_ratio , spent_hours

#############################
# 1. Read SSID and PW from SDCARD
# 2. Connect to WIFI
# 3. MAKE HTTP REQUEST
# 4. DISPLAY DATA ON SCREEN
#    REPEAT STEPS 3 & 4
#############################



# SSID , PW , NAME auslesen für Wifi Verbindung:
# Bsp: MyWIfi , 1234 , John Doe
def readfromsdcard():
    import os
    from machine import Pin, SPI
    from sdcard import SDCard

    spisd = SPI(-1, miso=Pin(13), mosi=Pin(12), sck=Pin(14))
    sd = SDCard(spisd, Pin(4))
    os.mount(sd, '/sd')
    print(os.listdir('/sd'))
    import json
    # read a config.json file that is on the sd card
    with open('/sd/config.json', 'r') as fs:
        c = json.loads(fs.read())
        label0 = M5TextBox(238, 449,  c['ssid'], lcd.FONT_DejaVu40, 0, rotate=0)





def do_connect(ssid,password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('OBI WLAN KENOBI', 'YOUR_PASSWORD')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def getData():
    import requests

    url = "https://support.lupcom.de/issues.json"

    payload={}
    headers = {
        'X-Redmine-API-Key': 'f8b3228f1149ee6df8261490403d8863f42aa94d',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)




lcd.show()