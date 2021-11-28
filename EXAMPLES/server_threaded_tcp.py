# A simple threaded server to recieve commands

def theaded_TCP():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('0.0.0.0', 7200)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(5)

    while True:
        # Wait for a connection
        connection, client_address = sock.accept()

        # indicator command recieved (turns led red for a second)
        rgb.setColorAll(0xff0000)
        rgb.setBrightness(3)

        # each connection becomes its own thread
        _thread.start_new_thread(threaded, (connection,))

#recievieng data and execute command
def threaded(connection):
    try:
        while True:
            data = connection.recv(1024)
            data = data.decode()

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
                    neopixel0.setColorFrom(1, 72, 0x66ffff)

                if data == 'rot':
                    neopixel0.setBrightness(1)
                    neopixel0.setColorFrom(1, 72, 0xff0000)

                if data == 'orange':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 72, 0xcc6600)

                if data == 'pink':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 72, 0xcc33cc)

                if data == 'gruen':
                    neopixel0.setBrightness(3)
                    neopixel0.setColorFrom(1, 72, 0x33cc00)

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