"""
All modules defined here
"""

from arbvisuals import clear, sleep
from colorama import init, Fore, Style
import os
init(convert=True)


def check_license(key="K3N0GR04B50910"):
    """
    checks whether the computer has access to the application
    :return:
    """
    try:
        os.system("attrib -h -r text.txt")
        os.system("wmic bios get serialNumber > text.txt")
        os.system("attrib +h +r text.txt")
        with open("text.txt", "rb") as sn:
            serial = sn.read().decode('utf-16')
        serial = serial.replace(" ", "")
        serial = serial.replace("\r\n", "")
        serial = serial.replace("SerialNumber", "")
        if serial != key:
            print(Fore.RED + Style.BRIGHT)
            print("\n" * 6 + "    " * 7 + "***ACCESS DENIED***")
            print("\n" + "    " * 6 + "***LICENSE KEY NOT FOUND***")
            print(Fore.GREEN + "\n" + " " * 10 + "contact <cliffygamy@gmail.com> to request a license key" + "\n" * 5)
            sleep(10)
            exit()
        else:
            print("allowed".upper())
            sleep(2)
            return 0

    except KeyboardInterrupt:
        clear()
        print(Fore.YELLOW + "\n "*2 + "License initialisation".upper())
        passcode = input(Fore.RESET + "\n "*2 + "ENTER PASSCODE: ")
        passcodes = ["[*%Baguvix]", "int m(void){}", "www.youtube0430.com"]
        if passcode not in passcodes:
            clear()
            print(Fore.RED + "\n" * 6 + "    " * 7 + "***ACCESS DENIED***")
            print(Fore.GREEN + "\n\n" + " " * 11 + "contact <cliffygamy@gmail.com> to request a license key" + "\n" * 5)
            sleep(10)
            exit()
        else:
            print("")


check_license()
