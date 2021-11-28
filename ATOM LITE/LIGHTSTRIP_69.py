import time
import machine

import network
import socket
import _thread
from m5stack import lcd
tft = lcd

import unit
neopixel0 = unit.get(unit.NEOPIXEL, unit.PORTA, 29)
# make sure not to double import when copy into uiflow :D


m5_device_list = \
    {
        "Core": {"width": 320, "height": 240},
        "Core2": {"width": 320, "height": 240},
        "StickC": {"width": 80, "height": 160},
        "StickCPlus": {"width": 135, "height": 240},
        "E-ink": {"width": 200, "height": 200},
        "Paper": {"width": 540, "height": 960},
    }

m5_device_list_noscreen = \
    {
        "Atom Lite": {"imu": False, },
        "Atom Matrix": {"imu": True, },
    }


# IDENTIFYING THE MODEL , BY SCREEN , or other unique characteristics
def GET_M5_MODEL():


    width, height = tft.screensize()



    for x in m5_device_list.items():
        if {"width": width, "height": height} in x:

            # since core/core2 have same screen ... we differntiate by import availabaility
            if x[1]['width'] == 320:
                try:
                    import m5stack_ui
                    return "Core 2"
                except:
                    try:
                        import base
                        return "Atom" # Atom Lite or matrix
                    except:
                        return "Core"
            return x[0]
    return "Unknown ESP32 Model"




# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
model = GET_M5_MODEL()
dhcp_hostname = nic.config(dhcp_hostname="Speaker_R_R") # changing default hostname to detected model
nic.connect('OBI WLAN KENOBI', 'winner11')
while not nic.isconnected(): pass
import socket



# To fix non responsive issues by itself until issue is identified
def automatic_restart():
    time.sleep(60 * 10) # Every 10 min
    machine.reset() # RESTARTING


def theaded_TCP():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # Bind the socket to the port
    server_address = ('0.0.0.0', 7200)
    print("info", socket.getaddrinfo('0.0.0.0' , 7200 ))
    print('starting up on %s port %s' % (server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(5)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        rgb.setColorAll(0xff0000) # indicator for looping
        rgb.setBrightness(3)


        print('connection from', client_address)
        _thread.start_new_thread(threaded, (connection,))

        # Receive the data in small chunks and retransmit it








def threaded(connection):
    try:
        while True:
            data = connection.recv(1024)
            data = data.decode()
            print(data)
            if data:
                if data == 'blau':
                    neopixel0.setBrightness(1)
                    neopixel0.setColorFrom(1, 29, 0x66ffff)

                if data == 'rot':
                    neopixel0.setBrightness(1)
                    neopixel0.setColorFrom(1, 29, 0xff0000)

                if data == 'orange':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 29, 0xcc6600)

                if data == 'pink':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 29, 0xcc33cc)

                if data == 'gruen':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 29, 0x33cc00)

                if data == 'on':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(15, 15, 0x33cc00)

                if data == 'shutdown':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(15, 15, 0xcc0000)
                    neopixel0.setColorFrom(1, 14, 0x000000)
                    neopixel0.setColorFrom(16, 29, 0x000000)
                if data == 'fullscreen':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(25, 29, 0xcc0000)
                    neopixel0.setColorFrom(1, 5, 0xcc0000)
                    neopixel0.setColorFrom(6, 24, 0x000000)
                if data == 'off':
                    neopixel0.setColorAll(0x000000)
                    # neopixel0.setBrightness(0)
                    # neopixel0.setColorFrom(1, 29, 0x000000)

            else:
                break

    finally:
        connection.close()
        rgb.setColorAll(0x000000)
        rgb.setBrightness(0)


theaded_TCP()
#_thread.start_new_thread(automatic_restart, ())