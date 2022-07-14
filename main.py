from sel_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def main():
    name = 'chromedriver.exe'
    root = 'C:/Users/simon/OneDrive/Desktop/Python'
    path = find(name, root).replace('\\', '/')

    driver = webdriver.Chrome(path)
    driver.get("https://www.skyscanner.it/")
    cookie = ClassWait(driver, By.ID, "acceptCookieButton", 20)
    cookie.WaitConditions()


    destination = ClassWait(driver, By.ID, "react-autowhatever-fsc-destination-search", 20)
    destination.WaitConditions()
    destination.clear()
    destination.send_keys("Lisbona")

    time.sleep(5000)




if __name__ == "__main__":
    main()
