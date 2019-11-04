import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Test():
   
   def setUpTest(self, driverTest):
      self.timeout = 10
      self.driver = webdriver.Chrome(ChromeDriverManager().install())
      self.driver.implicitly_wait(30)
      self.driver.maximize_window()

   def navigate(self):
      # Navigate to the application home page
      self.driver.get("https://www.gouletpens.com")

   def tearDown(self):
      self.driver.quit()



"""
# get the search textbox
#search_field = driver.find_element_by_name("q")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
#lists= driver.find_elements_by_class_name("r")

# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem.get_attribute("innerHTML"))
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()
"""