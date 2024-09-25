import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
import os
import random
from datetime import datetime

import requests
import windscribe

# with open("proxyList.txt","r") as f:
#     proxies = f.read().split("\n")
#
# sitesToCheck = ["https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html",
#                 "https://books.toscrape.com/catalogue/category/books/parenting_28/index.html",
#                 "https://books.toscrape.com/catalogue/category/books/romance_8/index.html"]
#
# counter = 0
#
# for site in sitesToCheck:
#     try:
#         print(f"Using the proxy: {proxies[counter]}")
#         res = requests.get(site, proxies={"http:": proxies[counter],
#                                           "https:": proxies[counter]})
#         print(res.status_code)
#     except:
#         print("Failed")
#     finally:
#         counter = counter + 1



def proxySwitcher():
    counter = -1
    with open("validProxies.txt", "r") as f:
        proxies = f.read().split("\n")
        print(proxies)
    counter = counter + 1
    print(f"Using the proxy: {proxies[counter]}")

    return proxies[counter]

def winscribeRotating():
    try:
        # Windscribe-Login mit deinen Benutzerdaten
        windscribe.login("luigi01791", "Windscribe002.")
        print("Erfolgreich eingeloggt.")

        # Zufällige Verbindung herstellen
        windscribe.connect(rand=True)
        print("Verbunden mit zufälliger IP.")

        # Status des Kontos abfragen
        print("Kontostatus:", windscribe.account())

        # 30 Sekunden warten, um sicherzustellen, dass die Verbindung stabil ist
        time.sleep(30)

        # VPN-Verbindung trennen
        windscribe.disconnect()
        print("Verbindung getrennt.")
    except Exception as e:
        print("Fehler bei der VPN-Verbindung:", str(e))



def windscribeIPRotation(action):
    connectList = ["US Central", "US East", "US West", "Canada East", "Canada West", "Germany", "France", "Norway",
                   "Romania", "Switzerland", "United Kingdom", "Switzerland", "Hong Kong"]
    windscribe_cli_path = r"C:\\Program Files\\Windscribe\\windscribe-cli.exe"
    if connectList is not None:
        location = random.choice(connectList)
        output = os.popen(f'"{windscribe_cli_path}" {action} {location}').read()
        print(output)


def main():
    # chrome_options = webdriver.ChromeOptions()
    # proxyToUse = proxySwitcher()
    # chrome_options.add_argument(f"--proxy-server={proxyToUse}")
    # url = "https://myexternalip.com/raw"
    # browser = webdriver.Chrome(options=chrome_options)
    # browser.get(url)
    res = requests.get("https://myexternalip.com/raw")
    print("Aktuelle IP-Adresse:", res.text.strip())
    print("Status Code:", res.status_code)

    # VPN verbinden und eine zufällige IP-Adresse zuweisen
    winscribeRotating()

    # IP-Adresse nach der VPN-Verbindung abrufen
    res = requests.get("https://myexternalip.com/raw")
    print("Neue IP-Adresse:", res.text.strip())
    print("Status Code:", res.status_code)

    # Wartezeit bis zum nächsten Wechsel
    time.sleep(40)

if __name__ == '__main__':
    # main()
    # windscribeTestin2()
    windscribeIPRotation("connect")

