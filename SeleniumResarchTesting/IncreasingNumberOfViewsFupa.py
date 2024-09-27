from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
import os
import random


url = "https://www.fupa.net/player/nv-leon-bohnlein-542430"

def windscribeIPRotation(action):
    connectList = ["US Central", "US East", "US West", "Canada East", "Canada West", "Germany", "France", "Norway",
                   "Romania", "Switzerland", "United Kingdom"]
    windscribe_cli_path = r"C:\\Program Files\\Windscribe\\windscribe-cli.exe"
    if connectList is not None:
        location = random.choice(connectList)
        print(location)
        output = os.popen(f'"{windscribe_cli_path}" {action} {location}').read()
        print(output)


def increaser():
    optionsEinstellungen = webdriver.ChromeOptions()
    optionsEinstellungen.add_argument("--disable-search-engine-choice-screen")
    optionsEinstellungen.add_argument("--icognito")
    driver = webdriver.Chrome(options=optionsEinstellungen)
    driver.get(url)
    time.sleep(2)
    try:
        cookiesAkzeptieren = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/span[2]/a").click()
    except:
        print("Keine Cookieanzeige vorhanden")
    finally:
        time.sleep(2)
        driver.close()
        print("Sauber durchgelaufen")


if __name__ == '__main__':
    counter = 0
    increasingClicks = 200
    # 7493
    while(counter < increasingClicks):
        windscribeIPRotation('connect')
        time.sleep(2)
        increaser()
        time.sleep(2)
        windscribeIPRotation('disconnect')
        counter = counter + 1
        print(counter)