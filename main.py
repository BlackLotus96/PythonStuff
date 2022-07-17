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
    root = 'C:/Users/simon/OneDrive/Desktop/Python'
    path = find(name, root).replace('\\', '/')
    driver = webdriver.Chrome(path)
    driver.get("https://www.kayak.it/")
    time.sleep(5)
    cookie = ClassWait(driver, By.XPATH, "/html/body/div[5]/div/div[3]/div/div/div[2]/div/div/div[1]/button", 10)
    cookie.WaitConditionsButtons()
    cookie = ClassWait(driver, By.XPATH, "/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[3]/div/div/input", 5)
    cookie.WaitConditionsInputBox("lisbona")

    time.sleep(20)

    #destination = ClassWait(driver, By.CLASS_NAME, "BpkInput_bpk-input__ZDdkM SingleDestControls_fsc-large-above-tablet__Mjg0Y SingleDestControls_fsc-docked-middle-above-tablet__MmIwM SingleDestControls_fsc-docked-last-on-tablet__MDI0N LocationSelector_fsc-location-input__NDRiO", 5)
    #destination.WaitConditionsInputBox()








if __name__ == "__main__":
    main()
