# import network
#
# wlan = network.WLAN(network.STA_IF) # create station interface
# wlan.active(True)       # activate the interface
# wlan.scan()             # scan for access points
# wlan.isconnected()      # check if the station is connected to an AP
# wlan.connect('essid', 'password') # connect to an AP
# wlan.config('mac')      # get the interface's MAC address
# wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses
#
# ap = network.WLAN(network.AP_IF) # create access-point interface
# ap.config(essid='ESP-AP') # set the ESSID of the access point
# ap.config(max_clients=10) # set how many clients can connect to the network
# ap.active(True)         # activate the interface


# # 访问ip地址 api
# r = requests.get("http://ip-api.com/json/")
# print(r)
# print(r.content)  # 返回响应的内容
# print(r.text)  # 以文本方式返回响应的内容
# print(r.content)
# print(r.json())  # 返回响应的json编码内容并转为dict类型

# r.close()


from m5stack import *
from m5ui import *
from uiflow import *
import time

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('OBI WLAN KENOBI', 'YOUR_PASSWORD')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def make_request():
    import urequests as requests
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Rostock&units=metric&APPID=c1748c3805b0b163e4b0e076934e505b")
    data = r.json()
    return data


def make_sleep():
    import machine
    # put the device to sleep for 10 seconds
    sleeptime = 30 * 60000 # 30 minutes
    machine.deepsleep(sleeptime)

########################################################
# APP
########################################################

# STEP 1
# CONNECT TO WIFI FIRST
do_connect()

# STEP 2
# MAKE REQUESTS
json_data = make_request()

# STEP 3
# GET THE DATA / FORMAT DATA
description = json_data['weather'][0]['description']
temp = str(json_data['main']['temp'])

setScreenColor(15)

# LINIE
#label0 = M5TextBox(459, -105, "Text", lcd.FONT_DejaVu24, 0, rotate=0)
#line0 = M5Line(M5Line.PLINE, 542, 507, 0, 507, 0)

#TEXT TEMPERATUR und ZAHL
label0 = M5TextBox(400, 50, temp, lcd.FONT_DejaVu72, 0, rotate=90)
label0 = M5TextBox(450, 50, "Temperatur", lcd.FONT_DejaVu40, 0, rotate=90)

#TEXT INFO und ZAHL
label0 = M5TextBox(150, 50, description, lcd.FONT_DejaVu72, 0, rotate=90)
label0 = M5TextBox(200, 50, "Info", lcd.FONT_DejaVu40, 0, rotate=90)
lcd.show()

time.sleep(3)

make_sleep()