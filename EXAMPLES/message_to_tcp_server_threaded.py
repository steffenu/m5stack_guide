import socket
import threading

# send a threaded message
# if no connection can be established
# throws Error Message ;)
def threaded_socket_message():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        eventghost_adress = ("192.168.1.100", 7200)
        sock.connect(eventghost_adress)

        message = 'pulse_red'
        sock.sendall(message.encode('utf-8'))


    except Exception as e:
        print("CIRI",e)
    finally:
        sock.close()

x = threading.Thread(target=threaded_socket_message, args=())
x.start()