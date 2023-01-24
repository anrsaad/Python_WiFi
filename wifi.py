# lists all WiFi and Passwords in your Computer 
# code by : Saad Anouar
# be sure you got the code from : https://github.com/anrsaad/Python_WiFi
import os

def animation():
    print("""         
                                               ___   ___  ___
      __███████ ]▄▄▄▄▄▄▄▄   -->> \\     /\\    /  |   |      | 
_▄▄▄▄▄█PASSWORDS█▄▄▄▄▄▄_          \\   /  \\  /   |   |---   | 
█████████████████████████].        \\ /    \\/   _|_  |     _|_ 
()▲()▲()▲()▲()▲()▲()▲()▲()                  By : [Saad Anouar]
    
""")

import subprocess
def wifi_profiles():
    data = subprocess.check_output(["netsh", "wlan","show","profiles"])
    str_data = data.decode("utf-8")
    str_data = str_data.splitlines()
    wifi = list()
    for line in str_data:
        if "All User Profile" in line :
            name = line.split(": ")[1]
            wifi.append(name)
    return wifi

os.system("@echo off")
os.system("color B")
os.system("cls")
animation()

print("\nYour Wifi Passwords :\n")
for name in wifi_profiles():
    data = subprocess.check_output(["netsh", "wlan", "show","profiles","name=", name, "key=clear" ])
    str_data = data.decode("utf-8", errors="backslashreplace")
    str_data = str_data.splitlines()
    wifi = list()
    for line in str_data:
        if "Key Content" in line :
            password = line.split(": ")[1]
    
    print(name, ": ", password)
print("\n")

# build using Pyinstaller, using this code :
# pyinstaller --ico C:\Users\anrsaad\Desktop\wifi.ico --onefile C:\Users\anrsaad\Desktop\wifi.py