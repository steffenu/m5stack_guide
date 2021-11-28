# SEND PAIRING REQUEST EVERY 30 Secs
def UDP_PAIRING_REQUEST(dhcp_hostname,mac_decoded,host_ip):
    broadcast_adress = ('192.168.1.255', 7200)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    m5_info = str({'dhcp_hostname': dhcp_hostname, 'mac': mac_decoded, 'host_ip': host_ip})

    global alive

    while alive == True :
        s.sendto(m5_info.encode('utf-8'), broadcast_adress)

        # recieving a stop message
        should_i_stop , addr2 = s.recv(1024) # recv = (bytes)
        time.sleep(30)