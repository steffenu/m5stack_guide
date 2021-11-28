import network
import socket
import _thread
import time

from m5stack import lcd
tft = lcd

import unit
neopixel0 = unit.get(unit.NEOPIXEL, unit.PORTA, 37)

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
dhcp_hostname = nic.config(dhcp_hostname="MONITOR") # changing default hostname to detected model
nic.connect('OBI WLAN KENOBI', 'winner11')
while not nic.isconnected(): pass
import socket



mode = 0


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

        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                data = data.decode()
                print(data)
                if data:
                    if data == 'error':
                        neopixel0.setBrightness(1)
                        neopixel0.setColor(1, 0xff0000)
                        neopixel0.setColor(4, 0xff0000)
                        neopixel0.setColor(6, 0xff0000)
                        neopixel0.setColor(8, 0xff0000)
                        neopixel0.setColorFrom(12, 13, 0xff0000)
                        neopixel0.setColor(19, 0xff0000)
                        neopixel0.setColorFrom(25, 26, 0xff0000)
                        neopixel0.setColor(30, 0xff0000)
                        neopixel0.setColor(32, 0xff0000)
                        neopixel0.setColor(34, 0xff0000)
                        neopixel0.setColor(37, 0xff0000)
                        neopixel0.setColorFrom(2, 3, 0x000000)
                        neopixel0.setColor(5, 0x000000)
                        neopixel0.setColor(7, 0x000000)
                        neopixel0.setColorFrom(9, 11, 0x000000)
                        neopixel0.setColorFrom(14, 18, 0x000000)
                        neopixel0.setColorFrom(20, 24, 0x000000)
                        neopixel0.setColorFrom(27, 29, 0x000000)
                        neopixel0.setColor(31, 0x000000)
                        neopixel0.setColor(33, 0x000000)
                        neopixel0.setColorFrom(35, 36, 0x000000)
                    if data == 'chrome':
                        neopixel0.setBrightness(3)

                        neopixel0.setColor(17, 0x336666)
                        neopixel0.setColor(21, 0x336666)
                        neopixel0.setColorFrom(6, 8, 0xff0000)
                        neopixel0.setColor(11, 0xffcc33)
                        neopixel0.setColor(14, 0xffcc33)
                    if data == 'speakers':
                        neopixel0.setBrightness(3)
                        neopixel0.setColorFrom(1, 4, 0x993399)
                        neopixel0.setColorFrom(34, 37, 0x993399)
                    if data == 'anime':
                        neopixel0.setBrightness(1)
                        neopixel0.setColor(8, 0x3366ff)
                        neopixel0.setColor(12, 0x3366ff)
                        neopixel0.setColor(17, 0x3366ff)
                        neopixel0.setColor(19, 0x3366ff)
                        neopixel0.setColor(25, 0x3366ff)
                        neopixel0.setColor(32, 0x3366ff)

                        neopixel0.setColorFrom(1, 7, 0x000000)
                        neopixel0.setColorFrom(9, 11, 0x000000)
                        neopixel0.setColorFrom(13, 16, 0x000000)
                        neopixel0.setColorFrom(20, 24, 0x000000)
                        neopixel0.setColorFrom(26, 31, 0x000000)
                        neopixel0.setColorFrom(33, 37, 0x000000)
                    if data == 'play_green':
                        neopixel0.setBrightness(1)
                        neopixel0.setColor(7, 0x33ff33)
                        neopixel0.setColorFrom(12, 13, 0x33ff33)
                        neopixel0.setColorFrom(18, 20, 0x33ff33)
                        neopixel0.setColorFrom(24, 27, 0x33ff33)
                        neopixel0.setColorFrom(1, 6, 0x000000)
                        neopixel0.setColorFrom(8, 11, 0x000000)
                        neopixel0.setColorFrom(14, 17, 0x000000)
                        neopixel0.setColorFrom(21, 23, 0x000000)
                        neopixel0.setColorFrom(28, 37, 0x000000)
                    if data == 'play_red':
                        neopixel0.setBrightness(1)
                        neopixel0.setColor(7, 0xff0000)
                        neopixel0.setColorFrom(12, 13, 0xff0000)
                        neopixel0.setColorFrom(18, 20, 0xff0000)
                        neopixel0.setColorFrom(24, 27, 0xff0000)
                        neopixel0.setColorFrom(1, 6, 0x000000)
                        neopixel0.setColorFrom(8, 11, 0x000000)
                        neopixel0.setColorFrom(14, 17, 0x000000)
                        neopixel0.setColorFrom(21, 23, 0x000000)
                        neopixel0.setColorFrom(28, 37, 0x000000)
                    if data == 'send':
                        neopixel0.setBrightness(1)
                        neopixel0.setColor(8, 0xff0000)
                        neopixel0.setColor(14, 0xff0000)
                        neopixel0.setColorFrom(17, 21, 0xff0000)
                        neopixel0.setColor(27, 0xff0000)
                        neopixel0.setColor(32, 0xff0000)
                        time.sleep(0.7)
                        neopixel0.setColorAll(0x000000)
                    if data == 'copy':
                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(12, 13, 0x33ff33)
                        neopixel0.setColor(18, 0x33ff33)
                        neopixel0.setColor(20, 0x33ff33)
                        neopixel0.setColorFrom(25, 26, 0x33ff33)
                        time.sleep(0.7)
                        neopixel0.setColorAll(0x000000)

                    if data == 'blau':
                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(12, 13, 0x33ccff)
                        neopixel0.setColorFrom(18, 20, 0x33ccff)
                        neopixel0.setColorFrom(25, 26, 0x33ccff)

                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(1, 11, 0x000000)
                        neopixel0.setColorFrom(14, 17, 0x000000)
                        neopixel0.setColorFrom(21, 24, 0x000000)
                        neopixel0.setColorFrom(27, 37, 0x000000)

                    if data == 'hellblau':
                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(12, 13, 0x33ffff)
                        neopixel0.setColorFrom(18, 20, 0x33ffff)
                        neopixel0.setColorFrom(25, 26, 0x33ffff)

                        neopixel0.setColorFrom(1, 11, 0x000000)
                        neopixel0.setColorFrom(14, 17, 0x000000)
                        neopixel0.setColorFrom(21, 24, 0x000000)
                        neopixel0.setColorFrom(27, 37, 0x000000)

                    if data == 'rot':
                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(12, 13, 0xff0000)
                        neopixel0.setColorFrom(18, 20, 0xff0000)
                        neopixel0.setColorFrom(25, 26, 0xff0000)

                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(1, 11, 0x000000)
                        neopixel0.setColorFrom(14, 17, 0x000000)
                        neopixel0.setColorFrom(21, 24, 0x000000)
                        neopixel0.setColorFrom(27, 37, 0x000000)

                    if data == 'orange':
                        neopixel0.setBrightness(3)
                        neopixel0.setColorFrom(12, 13, 0xcc6600)
                        neopixel0.setColorFrom(18, 20, 0xcc6600)
                        neopixel0.setColorFrom(25, 26, 0xcc6600)

                        neopixel0.setColorFrom(1, 11, 0x000000)
                        neopixel0.setColorFrom(14, 17, 0x000000)
                        neopixel0.setColorFrom(21, 24, 0x000000)
                        neopixel0.setColorFrom(27, 37, 0x000000)

                    if data == 'gruen':
                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(12, 13, 0x33ff33)
                        neopixel0.setColorFrom(18, 20, 0x33ff33)
                        neopixel0.setColorFrom(25, 26, 0x33ff33)

                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(1, 11, 0x000000)
                        neopixel0.setColorFrom(14, 17, 0x000000)
                        neopixel0.setColorFrom(21, 24, 0x000000)
                        neopixel0.setColorFrom(27, 37, 0x000000)

                    if data == 'on':
                        neopixel0.setBrightness(1)
                        neopixel0.setColor(19, 0x33ff33)
                        neopixel0.setColorFrom(1, 18, 0x000000)
                        neopixel0.setColorFrom(20, 37, 0x000000)

                    if data == 'shutdown':
                        neopixel0.setBrightness(1)
                        neopixel0.setColor(19, 0xff0000)
                        neopixel0.setColorFrom(1, 18, 0x000000)
                        neopixel0.setColorFrom(20, 37, 0x000000)
                    if data == 'fullscreen':
                        neopixel0.setBrightness(1)
                        neopixel0.setColorFrom(1, 5, 0xff0000)
                        neopixel0.setColorFrom(9, 10, 0xff0000)
                        neopixel0.setColorFrom(15, 16, 0xff0000)
                        neopixel0.setColorFrom(22, 23, 0xff0000)
                        neopixel0.setColorFrom(28, 29, 0xff0000)
                        neopixel0.setColorFrom(33, 37, 0xff0000)

                        neopixel0.setColorFrom(6, 8, 0x000000)
                        neopixel0.setColorFrom(11, 14, 0x000000)
                        neopixel0.setColorFrom(17, 21, 0x000000)
                        neopixel0.setColorFrom(24, 27, 0x000000)
                        neopixel0.setColorFrom(30, 32, 0x000000)

                    if data == 'loading_blau':
                        loading_youtube(0x66ffff)

                    if data == 'loading_hellblau':
                        loading_youtube(0x33ffff)

                    if data == 'loading_rot':
                        loading_youtube(0xff0000)

                    if data == 'loading_orange':
                        loading_youtube(0xcc6600)

                    if data == 'loading_pink':
                        loading_youtube(0xcc33cc)

                    if data == 'loading_gruen':
                        loading_youtube(0x33cc00)

                    if data == 'off':
                        neopixel0.setColorAll(0x000000)

                else:
                    break

        finally:
            # Clean up the connection
            connection.close()


def loading_youtube(color):
    global mode

    if mode == 0:
        mode += 1

        neopixel0.setBrightness(3)
        for x in range(38):
            neopixel0.setColor(x, color)
            time.sleep(0.01)

        for x in range(38):
            neopixel0.setColor(x, 0x000000)
            time.sleep(0.01)
    else:
        mode -= 1

        neopixel0.setBrightness(3)
        for x in reversed(range(38)):
            neopixel0.setColor(x, color)
            time.sleep(0.01)

        for x in reversed(range(38)):
            neopixel0.setColor(x, 0x000000)
            time.sleep(0.01)


theaded_TCP()