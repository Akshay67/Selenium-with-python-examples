from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

#For maximized the chrome window
chrome_options.add_argument("--start-maximized")

#To create the session for chrome browser
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

#Open url in browser
driver.get('http://www.google.co.in')

#to find the element by id
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

#Enter search keyword and submit
search_field.send_keys("selenium tutorials")
search_field.submit()

#get the list of element after search element
lists= driver.find_elements_by_class_name("_Rm")

#get the number of element found
print ("Found " + str(len(lists)) + "searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem)
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()
