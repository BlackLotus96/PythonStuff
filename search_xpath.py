from sel_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import sys
##
import time
#

def search(driver, times_of_pressure):
    if times_of_pressure == 1:
        cookie = ClassWait(driver, By.XPATH, "/html/body/header/div[1]/div/div/form/button", 10)
        cookie.WaitConditionsButtons()
        loopBodyXpath(driver)
    if times_of_pressure > 1:
        loopBodyXpath(driver)
#/html/body/main/section/div[3]/div[2]/div[3]/div[3]/a
#/html/body/main/section/div[3]/div[2]/div[5]/div[3]/a
def loopBodyXpath(driver):
    ListLabel = ["Espansione: ", "Nome ITA: ", "Nome ENG: ", "Disponibilità: ", "Prezzo: "]
    number_element = 0
    divs_path = "/html/body/main/section/div[3]/div[2]"
    divs_path_element = driver.find_element("xpath", divs_path)
    mat = [[] for _ in range(len(divs_path_element.find_elements(By.XPATH , "./*")))]

    for first_div in range(1, len(divs_path_element.find_elements(By.XPATH , "./*"))+1):
        first_div_path = divs_path+"/div["+str(first_div)+"]"
        first_div_path_element = driver.find_element(By.XPATH, first_div_path)
        print("@@@@@@@@@@@@@@@@@@")
        for second_div in range(1, len(first_div_path_element.find_elements(By.XPATH , "./*"))+1):
            second_div_path = first_div_path+"/div["+str(second_div)+"]"
            second_div_path_element = driver.find_element(By.XPATH, second_div_path)
            if second_div == 3:
                href_path = second_div_path+"/a"
                href = driver.find_element(By.XPATH, href_path)
                #print(href.get_attribute("data-original-title"))
            if second_div_path_element.text != "":
                mat[first_div-1].append(second_div_path_element.text)
    print(mat)
