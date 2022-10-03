from sel_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import sys
##
import time


def search(driver, times_of_pressure):
    if times_of_pressure == 1:
        cookie = ClassWait(driver, By.XPATH, "/html/body/header/div[1]/div/div/form/button", 10)
        cookie.WaitConditionsButtons()
        mat = loopBodyXpath(driver)
    if times_of_pressure > 1:
        mat = loopBodyXpath(driver)
    diz = formatMatrix(mat)
    json_object = json.dumps(diz, indent = 4) 
    print(json_object)
#/html/body/main/section/div[3]/div[2]/div[3]/div[3]/a
    #/html/body/main/section/div[3]/div[2]/div[5]/div[3]/a
def loopBodyXpath(driver):
    ListLabel = ["Espansione: ", "Nome ITA: ", "Nome ENG: ", "Disponibilità: ", "Prezzo: "]
    number_element = 0
    divs_path = "/html/body/main/section/div[3]/div[2]"
    divs_path_element = driver.find_element("xpath", divs_path)
    mat = [[] for _ in range(len(divs_path_element.find_elements(By.XPATH , "./*")))]
    i_mat = 0
    for first_div in range(1, len(divs_path_element.find_elements(By.XPATH , "./*"))+1):
        first_div_path = divs_path+"/div["+str(first_div)+"]"
        first_div_path_element = driver.find_element(By.XPATH, first_div_path)
        #print("@@@@@@@@@@@@@@@@@@")
        for second_div in range(1, len(first_div_path_element.find_elements(By.XPATH , "./*"))+1):
            second_div_path = first_div_path+"/div["+str(second_div)+"]"
            second_div_path_element = driver.find_element(By.XPATH, second_div_path)
            if second_div == 3:
                href_path = second_div_path+"/a"
                href = driver.find_element(By.XPATH, href_path)
                #print("first if: ", second_div)
                mat[i_mat].append(href.get_attribute("data-original-title"))
                #print(href.get_attribute("data-original-title"))
            if second_div_path_element.text != "":
                mat[i_mat].append(second_div_path_element.text)
        i_mat += 1
    #print(mat)
    return mat


def formatMatrix(mat):
    dict = {}
    for y in range(0, len(mat)):
        list_string_to_parse = mat[y][1].split("\n")
        ita_string = list_string_to_parse[0]
        eng_string = list_string_to_parse[1]
        mat[y][1] = ita_string
        mat[y].insert(2, eng_string)
        if mat[y][0] not in dict.keys():
            dict[mat[y][0]] = [mat[y][1:]]
        else:
            dict[mat[y][0]].append(mat[y][1:])
    return dict
