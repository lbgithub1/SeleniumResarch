import windscribe
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
import os
import random
import requests
import windscribe



# Aufrufe: 7.469 Leon
# Aufrufe: 8.731 Tim

# def proxySwitcher():
#     counter = -1
#     with open("proxyList.txt", "r") as f:
#         proxies = f.read().split("\n")
#
#     print(f"Using the proxy: {proxies[counter]}")
#     counter = counter +1
#     return proxies[counter]

def windscribeIPRotation(action):
    connectList = ["US Central", "US East", "US West", "Canada East", "Canada West", "Germany", "France", "Norway",
                   "Romania", "Switzerland", "United Kingdom"]
    windscribe_cli_path = r"C:\\Program Files\\Windscribe\\windscribe-cli.exe"
    if connectList is not None:
        location = random.choice(connectList)
        print(location)
        output = os.popen(f'"{windscribe_cli_path}" {action} {location}').read()
        print(output)
def increaseClicks(number):
    i = 0
    while i < number:
        windscribeIPRotation('connect')
        time.sleep(2)
        nameForLookUp = "Leon Böhnlein"
        optionsEinstellungen = webdriver.ChromeOptions()
        optionsEinstellungen.add_argument("--disable-search-engine-choice-screen")
        driver = webdriver.Chrome(options=optionsEinstellungen)

        driver.get("https://www.fupa.net/search")
        time.sleep(3)

        cookiesAkzeptieren = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/span[2]/a").click()
        time.sleep(2)

        searchBar = driver.find_element(By.XPATH, "//input[@id='search' and @name='search']")
        searchBar.click()
        time.sleep(2)
        for letter in nameForLookUp:
            time.sleep(0.04)
            searchBar.send_keys(letter)

        time.sleep(3)
        player = driver.find_element(By.CLASS_NAME, "jOiTFY").click()

        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(2)
        print("Ok sauber")
        driver.close()
        windscribeIPRotation('disconnect')
        print(i)
        i+=1
        time.sleep(2)

if __name__ == '__main__':
    # for i in range (0,10):
    #     windscribeIPRotation("connect")
    #     time.sleep(3)
    #     increaseClicks()
    #     windscribeIPRotation("disconnect")
    #     i = i+1
    #     print(i)
    increaseClicks(10)