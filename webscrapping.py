from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import sys 
driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
driver.get("https://www.amazon.in/")
print(driver.title)
search_bar = driver.find_element_by_id("twotabsearchtextbox")
search_bar.clear()
search_bar.send_keys("OnePlus Nord CE 2 5G")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
! pip install webdriver_manager
# Select custom Chrome options
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
# Open the Chrome browser
browser = webdriver.Chrome(webdriver_path, options=options)
browser.get(amazon_url)
from selenium.webdriver.common.by import By
search_bar = browser.find_element(By.ID,"twotabsearchtextbox")
search_bar.send_keys(search_item)
search_bar.submit
