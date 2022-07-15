from sel_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time
import os


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def main():
    #options = Options()
    #options.headless = True

    name = 'chromedriver.exe'
    root = 'C:/Users/simone.meddi/Desktop/Simone'
    path = find(name, root).replace('\\', '/')
    driver = webdriver.Chrome(path)
    driver.get("https://www.skyscanner.it/")
    #holdBot = ClassWait(driver, By.ID, "QDqceQXfNxsWMOn", 20)
    time.sleep(10)
    cookie = ClassWait(driver, By.ID, "acceptCookieButton", 10)
    cookie.WaitConditions().click()

    destination = ClassWait(driver, By.CLASS_NAME, "BpkInput_bpk-input__ZDdkM SingleDestControls_fsc-large-above-tablet__Mjg0Y SingleDestControls_fsc-docked-middle-above-tablet__MmIwM SingleDestControls_fsc-docked-last-on-tablet__MDI0N LocationSelector_fsc-location-input__NDRiO", 5)
    destination.WaitConditions().clear().send_keys("Lisbona")







if __name__ == "__main__":
    main()
