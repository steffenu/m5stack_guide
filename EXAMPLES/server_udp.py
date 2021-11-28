
def UDP_SERVER(dhcp_hostname,mac_decoded,host_ip):
    port = 7300

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host_ip[0], port))  # make sure to change to device IP

    while True:
        data, addr = s.recvfrom(1024)
        decoded_data = data.decode()

        # IF THERE IS ANY DATA
        if data:

            try:
                """
                {'host_port': 7300, 'broadcast_adress': '192.168.1.255', 'host_name': 'NewSilver',
                               'host_mac': 'D0:50:99:3B:49:00', 'host_ip': '192.168.1.101'}
                """
                # DO SOMETHING WHEN MESSAGE IS RECCIEVED

            except Exception as e:

                label0 = M5TextBox(20, 10, str("Error in UDP_SERVER"), lcd.FONT_Default, 0xFFFFFF, rotate=0)
                label9 = M5TextBox(0, 30, str(e), lcd.FONT_Default, 0xFFFFFF, rotate=0)

                printError(e)


## prints error message nicely to m5core screen
def printError(e):
    import sys;
    from uio import StringIO
    s = StringIO();
    sys.print_exception(e, s)
    s = s.getvalue();
    s = s.split('\n')
    line = s[1].split(',');
    line = line[1];
    error = s[2];
    err = error + line;
    label12 = M5TextBox(0, 60, str(err), lcd.FONT_Default, 0xFFFFFF, rotate=0)