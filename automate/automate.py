import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class NBTC_Automation:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = self.initialize_driver()
        self.login_url = "https://fmr.nbtc.go.th/"
        self.relative_path = "automate/fco_data"
        self.working_directory = os.getcwd()
        self.absolute_path = os.path.join(
            self.working_directory, self.relative_path)

    def initialize_driver(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        return driver

    def login(self):
        self.driver.get(self.login_url)
        user_input = self.driver.find_element(By.ID, "UserName")
        password_input = self.driver.find_element(By.ID, "Password")
        login_button = self.driver.find_element(By.ID, "bLogin")

        user_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button.click()

    def navigate_to_dms(self):
        try:
            click_dms = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div/div/div/div[2]/a"))
            )
            click_dms.click()
        except TimeoutException:
            print("DMS link was not available within the given time.")

    def navigate_to_occ(self):
        try:
            click_occ = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//img[@src='asset/oper.svg']"))
            )
            click_occ.click()
            click_nav = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[text()='งานตรวจสอบคลื่นความถี่']"))
            )

            click_nav.click()

        except Exception as e:
            print("An error occurred.", e)

    def upload_files(self):
        for file_name in os.listdir(self.absolute_path):
            file_path = os.path.join(self.absolute_path, file_name)
            self.upload_file(file_path)
            self.save_file()
            self.confirm_upload()

    def upload_file(self, file_path):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "menu_station214708")))
        monitoring_system = self.driver.find_element(
            By.ID, "menu_station214708")
        monitoring_system.click()

        upload_field = self.driver.find_element(By.ID, "File1")
        upload_field.send_keys(file_path)

        preview_button = self.driver.find_element(By.ID, "bPreview")
        preview_button.click()

    def save_file(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "bSave"))
        )
        save_button.click()

    def confirm_upload(self):
        done_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                # ("//div[@class='row-40percent']/a[contains(text(),'Earn upto 2.5%')]")
                (By.XPATH, "/html/body/div[4]/div/div[10]/button[1]"))
        )
        done_button.click()

    def run_dms(self):
        self.login()
        self.navigate_to_dms()
        self.upload_files()

    def close(self):
        self.driver.quit()

    def run_occ(self):
        self.login()
        self.navigate_to_occ()


if __name__ == "__main__":
    automation = NBTC_Automation("tossakun.y", "022135Bon!")
    # automation.run_dms()
    automation.run_occ()
    # Consider uncommenting the line below if you want to close the browser automatically after the run.
    # automation.close()
