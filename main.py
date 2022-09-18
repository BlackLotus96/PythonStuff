from sel_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys
#
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
    root = r"C:\Users\simon\OneDrive\Desktop\Python\PythonDriver"
    path = find(name, root).replace('\\', '/')
    #chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path)
    driver.get("https://www.cardmarket.com/it/Magic")
    #time.sleep(20)
    #sys.exit()

    cookie = ClassWait(driver, By.XPATH, "/html/body/header/div[1]/div/div/form/button", 10)
    cookie.WaitConditionsButtons()

    tbody_XPATH = "/html/body/main/section[2]/div/div[2]/div[1]/table/tbody"
    tbody = driver.find_element("xpath", tbody_XPATH)

    for i_tr in range(1, len(tbody.find_elements(By.XPATH , "./*"))+1):
        tr_XPATH = tbody_XPATH+"/tr["+str(i_tr)+"]"
        tr = driver.find_element("xpath", tr_XPATH)
        print("@@@@@@@@@@@@@@@@@@")
        for i_td in range(1, len(tr.find_elements(By.XPATH , "./*"))+1):
            td_XPATH = tr_XPATH+"/td["+str(i_td)+"]"
            td = driver.find_element("xpath", td_XPATH)
            print(td.text)

    '''
    element = driver.find_element("xpath", "/html/body/main/section[2]/div/div[2]/div[1]/table/tbody/tr[4]")
    print(element)
    text = driver.find_element("xpath", "/html/body/main/section[2]/div/div[2]/div[1]/table/tbody/tr[4]/td[4]")
    print(text.text)
    '''

    while True:
        pass
    '''
    cookie = ClassWait(driver, By.XPATH, "/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/input", 5)
    cookie.WaitConditionsInputBox("lisbona")
    '''

    #destination = ClassWait(driver, By.CLASS_NAME, "BpkInput_bpk-input__ZDdkM SingleDestControls_fsc-large-above-tablet__Mjg0Y SingleDestControls_fsc-docked-middle-above-tablet__MmIwM SingleDestControls_fsc-docked-last-on-tablet__MDI0N LocationSelector_fsc-location-input__NDRiO", 5)
    #destination.WaitConditionsInputBox()



if __name__ == "__main__":
    main()
