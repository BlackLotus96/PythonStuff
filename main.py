from sel_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    PATH = "C:/Users/simon/OneDrive/Desktop/Python/PythonDriver/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.eurobet.it/it/scommesse/#!/")
    wait_class_1 = ClassWait(driver, By.ID, "onetrust-accept-btn-handler", 20)
    wait_class_1.WaitConditions()
    wait_class_2 = ClassWait(driver, By.ID, "att_lightbox_close", 20)
    wait_class_2.WaitConditions()





if __name__ == "__main__":
    main()
