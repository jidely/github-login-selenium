from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def sigIn(self):
        self.browser.get('https://github.com/login')
        self.browser.maximize_window()
        time.sleep(2)

        username = self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        password = self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)

        time.sleep(2)

        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[11]").click()

        time.sleep(2)

   


github = Github(username,password)
github.sigIn()
        
