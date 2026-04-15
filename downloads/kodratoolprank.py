#!/usr/bin/env python3
# Kodra – Hacker Style Terminal Panel (Simulation Only)

import os
import time
import random
from colorama import Fore, Style

def clear():
    os.system("clear")

def banner():
    print(Fore.GREEN + """
██   ██  ██████  ██████  ██████   █████  ██████
██   ██ ██    ██ ██   ██ ██   ██ ██   ██ ██   ██
███████ ██    ██ ██████  ██████  ███████ ██████
██   ██ ██    ██ ██   ██ ██   ██ ██   ██ ██   ██
██   ██  ██████  ██   ██ ██   ██ ██   ██ ██   ██
            K O D R A   F R A M E W O R K
""" + Style.RESET_ALL)

def loading(text, speed=0.05):
    for i in range(1, 28):
        print(Fore.CYAN + f"{text} [{i*4}%]" + Style.RESET_ALL, end="\r")
        time.sleep(speed)
    print()

def random_pass():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(10))

def insta_bruteforce():
    clear()
    banner()

    print(Fore.YELLOW + "Instagram Attack Module" + Style.RESET_ALL)
    user = input(Fore.CYAN + "\nTarget username: " + Style.RESET_ALL)

    print()
    loading("Connecting to Instagram servers")
    loading("Checking security layers")
    loading("Initializing brute‑force engine")
    loading("Launching attack")

    print(Fore.RED + "\nAccess granted!" + Style.RESET_ALL)
    time.sleep(0.6)

    password = random_pass()

    print(Fore.GREEN + f"""
TARGET     : {user}
PASSWORD   : {password}
STATUS     : SUCCESS
""" + Style.RESET_ALL)

    input(Fore.YELLOW + "\nPress ENTER to return..." + Style.RESET_ALL)


def wifi_attack():
    clear()
    banner()

    print(Fore.YELLOW + "WiFi Network Penetration Module" + Style.RESET_ALL)
    print()

    # Simulated WiFi SSID pull
    ssid = os.popen("getprop wifi.interface").read().strip()
    if not ssid:
        ssid = "Android_WiFi_AP"

    print(Fore.CYAN + f"Connected Network: {ssid}" + Style.RESET_ALL)
    print()

    loading("Scanning router ports")
    loading("Dumping WPA handshake")
    loading("Cracking key with wordlist")
    loading("Decrypting password", 0.07)

    # Fake cracked password
    wifi_pass = random_pass()

    print(Fore.GREEN + f"""
NETWORK     : {ssid}
PASSWORD    : {wifi_pass}
SECURITY    : WPA2-PSK
STATUS      : DECRYPTED
""" + Style.RESET_ALL)

    input(Fore.YELLOW + "\nPress ENTER to return..." + Style.RESET_ALL)


def main_menu():
    while True:
        clear()
        banner()

        print(Fore.MAGENTA + """
[1] Instagram Password Attack  
[2] WiFi Password Decryption  
[0] Exit
""" + Style.RESET_ALL)

        choice = input(Fore.CYAN + "Select: " + Style.RESET_ALL)

        if choice == "1":
            insta_bruteforce()

        elif choice == "2":
            wifi_attack()

        elif choice == "0":
            clear()
            print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
            time.sleep(0.4)
            break

        else:
            print(Fore.RED + "Incorrect option!" + Style.RESET_ALL)
            time.sleep(1)


if __name__ == "__main__":
    main_menu()