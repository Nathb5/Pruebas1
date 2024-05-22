from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Chrome()
driver.get("https://giphy.com/")
driver.maximize_window()
time.sleep (6)
driver.find_element (By.NAME, "sc-bZHSxH dRhWeq" ).send_keys("morat")
time.sleep(10)
