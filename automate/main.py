from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.options import Options

import time 
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://fmr.nbtc.go.th/NBTCROS/Login.aspx")



#id
user  = driver.find_element(By.ID, "UserName")
password =  driver.find_element(By.ID, "Password")
#login
click_login = driver.find_element(By.ID, "bLogin")



user.send_keys("puvakrint.p")
time.sleep(3)
password.send_keys("Dearxcore555#@")
time.sleep(3)
click_login.click()