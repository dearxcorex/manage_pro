from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

from selenium.webdriver.chrome.options import Options

import time 
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://fmr.nbtc.go.th/NBTCROS/Login.aspx")

# #id
user  = driver.find_element(By.ID, "UserName")
password =  driver.find_element(By.ID, "Password")
#login
click_login = driver.find_element(By.ID, "bLogin")


# #auto login
user.send_keys("puvakrint.p")
time.sleep(3)
password.send_keys("Dearxcore555#@")
time.sleep(3)
click_login.click()

# #click dms 
click_dms =driver.find_element(By.XPATH, "/html/body/div[@class='container-fluid nbtcros-container p-4 d-flex flex-column']/div[@class='container my-4']/div[@class='row']/div[@class='col-12 col-md-6 col-lg-4 my-3'][2]/a[@class='d-flex align-items-center justify-content-center nbtcros-sectionpage--item']")

time.sleep(3)
click_dms.click()

#upload file 
relative_path = "fco_data/pro_9.csv"
working_directory = os.getcwd()
absolute_path = os.path.join(working_directory, relative_path)
upload_file  = driver.find_element(By.ID, "File1")

upload_file.send_keys(f"{absolute_path}")
                        



