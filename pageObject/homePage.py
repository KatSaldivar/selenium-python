import os, test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
 
def accountButton(self): 
    self.driver.find_element_by_class_name("header__account-nav-link--account")

def getPageTitle(self):
    titleArea=self.driver.find_element_by_class_name("page-title")
    return titleArea.getText()