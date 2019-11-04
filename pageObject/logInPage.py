from functional import test
import homePage

def emailField(self): 
    self.driver.find_element_by_id("CustomerEmail")

def passwordField(self): 
    self.driver.find_element_by_id("CustomerPassword")

def submitButton(self): 
    self.driver.find_element_by_type("submit")