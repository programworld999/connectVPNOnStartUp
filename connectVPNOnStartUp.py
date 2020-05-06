import requests
import time
import os

def connectVPN():
    connected = False
    try:
        os.system("windscribe connect")
        connected = True
    except :
        connected = False
    return connected

if __name__ == "__main__":
    loop_value = 1
    while (loop_value):
        try:
            requests.get("http://google.com")
        except:
            print("Network currently down.")
        else:
            print("Up and running.")
            loop_value = 0
            if(connectVPN()):
                print("\033[0m|\033[1;32;40m VPN Connected! \033[0m")
            else:
                print("\033[0m|\033[0;37;41m VPN Not Connected \033[0m")
        time.sleep(2)