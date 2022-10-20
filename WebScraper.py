#wall of imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
#import pandas as pd      # use this for analyzing data?
#import pygsheets as ps   # use this to analyze data?

#NOTE: timers may not work if ads are too chunky. just reload the script at this point
#NOTE: see todo below


PATH = "C:\Program Files (x86)\chromedriver.exe" #this is where I put my chromedriver; it's dif for everyone
driver = webdriver.Chrome(PATH) 

stockList = ['SPY'] #current test stock list is size 1. SPY is an ETF that tracks the S&P 500

i = 0
while i < len(stockList): #look up all the stonks
    openYFi = driver.get('https://finance.yahoo.com/')
    searchBox = driver.find_element_by_id('yfin-usr-qry') #this is what the search bar is called. found from f12 and inspecting element on the page.
    searchBox.send_keys("{0}".format(stockList[i])) #send in current value of the stock list
    time.sleep(3) #wait 3 secs for loading
    stockPg = searchBox.send_keys(Keys.RETURN)
    time.sleep(4) #wait 3 secs for loading
    i+=1 

#TODO: uhh i think the stuff below should be in the loop
#whatever that's a prob for later

histData = driver.find_element(By.XPATH, '//span[text()="Historical Data"]').click() #look for 1y hist. data
time.sleep(3) 
clickApply = driver.find_element(By.XPATH, '//span[text()="Apply"]').click() #confirm the time length

downloadData = driver.find_element(By.XPATH, '//span[text()="Download"]').click() #download csv file of data
time.sleep(5) #wait 5 secs for download.  this can change if the computer/wifi is bad
driver.close() 
i+=1 #if i move the above chunk into the while just delete this



#TODO: now it downloads a csv file that only works in google sheets
