from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#PROVA

PATH = "C:/Users/simon/OneDrive/Desktop/Python/PythonDriver/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.eurobet.it/it/scommesse/#!/")

try:
	cookie_accepted = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located(('id', "onetrust-accept-btn-handler"))
		)
finally:
	cookie_accepted.click()

try:
	bonus = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located(('id', "att_lightbox_close"))
		)
finally:
	bonus.click()
