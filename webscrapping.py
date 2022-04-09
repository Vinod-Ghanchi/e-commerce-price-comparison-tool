from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import sys 
webdriver_path = 'D:/chromedriver_win32/chromedriver.exe' # Enter the file directory of the Chromedriver
amazon_url = 'https://www.amazon.in/'
search_item = 'OnePlus Nord CE 2 5G' 
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
