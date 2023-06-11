from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoAlertPresentException

import time 
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("www")

# #id
user  = driver.find_element(By.ID, "UserName")
password =  driver.find_element(By.ID, "Password")
#login
click_login = driver.find_element(By.ID, "bLogin")


# #auto login
user.send_keys("YourUsername")
time.sleep(3)
password.send_keys("YourPassword")
time.sleep(3)
click_login.click()

# #click dms 
#uToken("https://afm.nbtc.go.th/AFM","/DMS")
click_dms =driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/a")

time.sleep(3)
click_dms.click()

#choose Monitoring system
monitoring_sysytem = driver.find_element(By.XPATH,"//a[@id='menu_station214708']")
monitoring_sysytem.click()


#process all pro 

#upload file 
relative_path = "fco_data/test_9.csv"
working_directory = os.getcwd()
absolute_path = os.path.join(working_directory, relative_path)
upload_file  = driver.find_element(By.ID, "File1")
print(absolute_path)
upload_file.send_keys(f"{absolute_path}")

#Click Preview 
click_preview =  driver.find_element(By.XPATH,"//input[@id='bPreview']")
time.sleep(3)
click_preview.click()

#click Save
click_save = driver.find_element(By.XPATH,"//input[@id='bSave']")
click_save.click()


#click done 
# popup = driver.switch_to.alert
# popup.accept()
click_done = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[10]/button[1]")
click_done.click()






