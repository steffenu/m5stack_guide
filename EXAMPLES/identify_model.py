

# EXPERIMENTAL FUNCTION TO IDENTIFY M5STACK MODELS
# SOME MODELS HAVE IDENTICAL SCREEN OR NONE ... SO
# WE LOOK FOR DIFFERENCES ..
# UNTIL M5STACK has its own model indentifcation function ....
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