import bluetooth
bluetooth_devices = bluetooth.discover_devices(lookup_names=True)
for name in bluetooth_devices:
    print("address of the device is:",name)
    #print("name of the device is :", name)
    # print(bluetooth.ADVANCED_AUDIO_CLASS)
    # # print(bluetooth.GENERIC_TELEPHONY_PROFILE)
    if  bluetooth.ADVANCED_AUDIO_CLASS:
        print("pass")
    else:
        print("fail")

