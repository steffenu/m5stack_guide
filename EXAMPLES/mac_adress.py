import ubinascii
import network
import wifiCfg
import deviceCfg
import os

# your credentials that you flashed onto the device via BURNER SOFTWARE
SSID, PASS = wifiCfg.deviceCfg.wifi_read_from_flash()

# # your credentials that you flashed onto the device via BURNER SOFTWARE
deviceCfg.get_wifi_list()

# your device mac adress (unformatted)
mac = nic.config('mac')

# your device mac adress (formatted nicely)
mac_decoded = ubinascii.hexlify(mac, ':').decode()

# your m5 device ip adress
host_ip = list(nic.ifconfig()) # return a tuple json doesnt allow tuple

# machine = M5stack with Esp32 nodename=eps32 , release = 1.12.0
os.uname()

