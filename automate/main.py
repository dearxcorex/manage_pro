import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time 
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("")

#find box id pass
user  = driver.find_element(By.ID, "UserName")
password =  driver.find_element(By.ID, "Password")

#login
click_login = driver.find_element(By.ID, "bLogin")


#send id password  login
user.send_keys("")
time.sleep(3)
password.send_keys("")
time.sleep(3)
click_login.click()

# #click dms 

click_dms =driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/a")

time.sleep(3)
click_dms.click()




#-------process all pro--------

#upload file 
relative_path = "fco_data"
working_directory = os.getcwd()
absolute_path = os.path.join(working_directory, relative_path)

for file_name in os.listdir(absolute_path):
    #choose Monitoring system
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='menu_station214708']")))
    monitoring_sysytem = driver.find_element(By.XPATH,"//a[@id='menu_station214708']")
    monitoring_sysytem.click()
    print(" Pick  ภภ.เขต 23 - A-23-nakhon ratchasima (Remote Station)")
    
    file_path = os.path.join(absolute_path,file_name)

    upload_file  = driver.find_element(By.ID, "File1")
    upload_file.send_keys(f"{file_path}")
    print(f'upload: { file_path}')
    #Click Preview 
    click_preview =  driver.find_element(By.XPATH,"//input[@id='bPreview']")
    time.sleep(3)
    click_preview.click()
    print("Click Preview")
    #click Save
    click_save = driver.find_element(By.XPATH,"//input[@id='bSave']")
    click_save.click()
    print("Click Save")

    #click done 
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/div[10]/button[1]")))
    click_done = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[10]/button[1]")
    click_done.click()
    print("Click Done ")






