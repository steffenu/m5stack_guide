def make_sleep():
    import machine
    # put the device to sleep for 10 seconds
    sleeptime = 30 * 60000 # 30 minutes
    machine.deepsleep(sleeptime)