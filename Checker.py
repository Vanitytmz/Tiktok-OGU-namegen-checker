from requests.exceptions import ProxyError
from colorama import Fore, Back, Style
import requests
import threading
import random
import os
from os import system
coolscript = 'Tikok Username Checker By Vanity/*\Made For OGU Retards'
system("title Tikok Username Checker By Vanity/*\Made For OGU Retards")

def start():
    while True:
        http_proxy = "http://user:pass@hostname:port"
        https_proxy = "http://user:pass@hostname:port"
        proxyDict = {
        "http": http_proxy,
        "https": https_proxy,
        }
        lines = open('txt.txt').read().splitlines()
        username = random.choice(lines)
        url = 'https://www.tiktok.com/@'+username
        response = requests.get(url, proxies=proxyDict)
        if response.status_code == 200:
            print(Fore.YELLOW+"Username <"+Fore.LIGHTMAGENTA_EX+username+Fore.RED+"> is taken"+'\n')
        else:
            print(Fore.LIGHTMAGENTA_EX+username+Fore.GREEN+" is available")
            os.system("pause")

threads = []

for i in range(40):
    t = threading.Thread(target=start)
    t.daemon = True
    threads.append(t)

for i in range(40):
    threads[i].start()

for i in range(40):
    threads[i].join()
