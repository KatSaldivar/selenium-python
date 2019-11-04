import test 
from pageObject import homePage, logInPage

def test__login(self):
   self.setUpTest
   self.homePage.accountButton.click()
   self.logInPage.emailField.send_keys("email@gmail.com")
   self.logInPage.passwordField.send_keys("password")
   assert self.logInPage.getpageTitle == "My Account"
   self.test.tearDown

def test__logout(self):
   self.setUpTest
   self.homePage.accountButton.click()
   self.logInPage.emailField.send_keys("email@gmail.com")
   self.logInPage.passwordField.send_keys("password")
   self.accountPage.signoutButton.click()
   assert self.homePage.accountButton.getText() == "My Account"
   self.test.tearDown