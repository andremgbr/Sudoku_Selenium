from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main import resolve
import time
import numpy as np


driver = webdriver.Chrome("chromedriver_win32\\chromedriver")
wait = WebDriverWait(driver,3000)


driver.get('https://www.sudokupeople.com/')


try:
	element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="board"]/div[1]/div[1]/div[2]/div[1]/div[1]')))
finally:
	entry = driver.find_element_by_xpath('//*[@id="board"]/div[1]/div[1]/div[2]/div[1]/div[1]' )
	time.sleep(5)
	entry.send_key('9')

