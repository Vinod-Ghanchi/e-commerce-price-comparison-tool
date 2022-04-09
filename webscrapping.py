from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import sys 
webdriver_path = 'C:/Users/sidha/Downloads/chromedriver_win32/chromedriver.exe' # Enter the file directory of the Chromedriver
flipkart_url = 'https://www.flipkart.com/'
search_item = 'IQOO Z5 5G' # Chose this because I often search for phones!
options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
# Open the Chrome browser
browser = webdriver.Chrome(webdriver_path, options=options)
browser.get(flipkart_url)
