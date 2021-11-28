import json


# read a config.json file that is on the sd card
with open('/sd/config.json', 'r') as fs:
    c = json.loads(fs.read())
    label0 = M5TextBox(140, 106, c['ssid'], lcd.FONT_Default, 0xFFFFFF, rotate=0)




