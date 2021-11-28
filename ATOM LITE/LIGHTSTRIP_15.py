import time
import machine

import network
import socket
import _thread
from m5stack import lcd
tft = lcd

import unit
neopixel0 = unit.get(unit.NEOPIXEL, unit.PORTA, 72)
# make sure not to double import when copy into uiflow :D
mode = 0

# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
dhcp_hostname = nic.config(dhcp_hostname="Bett") # changing default hostname to detected model
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



def loading_youtube(color):
    global mode

    if mode == 0:
        mode += 1

        neopixel0.setBrightness(3)
        for x in range(29):
            neopixel0.setColor(x, color)
            time.sleep(0.001)

        for x in range(29):
            neopixel0.setColor(x, 0x000000)
            time.sleep(0.001)
    else:
        mode -= 1

        neopixel0.setBrightness(3)
        for x in reversed(range(29)):
            neopixel0.setColor(x, color)
            time.sleep(0.001)

        for x in reversed(range(29)):
            neopixel0.setColor(x, 0x000000)
            time.sleep(0.001)



def fullscreen_youtube(color):
    for x in range(15):
        neopixel0.setColor(15 + x, color)
        neopixel0.setColor(15 - x, color)
        neopixel0.setBrightness(3)
        time.sleep(0.001)

    for x in range(15):
        neopixel0.setColor(15 + x, 0x000000)
        neopixel0.setColor(15 - x, 0x000000)
        time.sleep(0.001)






def threaded(connection):
    try:
        while True:
            data = connection.recv(1024)
            data = data.decode()
            print(data)
            if data:
                if data == 'pulse_red':
                    fullscreen_youtube(0xff0000)

                if data == 'pulse_blue':
                    fullscreen_youtube(0x66ffff)

                if data == 'pulse_orange':
                    fullscreen_youtube(0xcc6600)

                if data == 'pulse_gruen':
                    fullscreen_youtube(0x33cc00)

                if data == 'blau':
                    neopixel0.setBrightness(1)
                    neopixel0.setColorFrom(1, 15, 0x66ffff)

                if data == 'rot':
                    neopixel0.setBrightness(1)
                    neopixel0.setColorFrom(1, 15, 0xff0000)

                if data == 'orange':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorAll(0xcc9933)

                if data == 'pink':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 15, 0xcc33cc)

                if data == 'gruen':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 15, 0x33cc00)

                if data == 'on':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(7, 7, 0x33cc00)

                if data == 'shutdown':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(7, 7, 0xcc0000)
                    neopixel0.setColorFrom(1, 6, 0x000000)
                    neopixel0.setColorFrom(8, 15, 0x000000)
                if data == 'fullscreen':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 3, 0xcc0000)
                    neopixel0.setColorFrom(13, 15, 0xcc0000)
                    neopixel0.setColorFrom(4, 11, 0x000000) # off
                if data == 'off':
                    neopixel0.setBrightness(0)
                    neopixel0.setColorFrom(1, 15, 0x000000)

                else:
                    break

    finally:
        connection.close()
        rgb.setColorAll(0x000000)
        rgb.setBrightness(0)


theaded_TCP()
#_thread.start_new_thread(automatic_restart, ())


