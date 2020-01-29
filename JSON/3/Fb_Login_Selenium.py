"""
How to Create Test Scripts in Selenium with Python

In this example, we did automation for "Facebook login page" using the Firefox driver.

EXAMPLE 1: Login into Facebook 
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()

"""
Explanation of the code

    Code line 1: From selenium module import webdriver
    Code line 2: From selenium module import Keys
    Code line 3: User is a variable which will be we used to store values of username.
    Code line 4: Variable "password" will be used to store values of the password.
    Code line 5: In this line, we are initializing "FireFox" by making an object of it.
    Code line 6: The "driver.get method" will navigate to a page given by the URL. WebDriver will wait until the page has been completely loaded (that is, the "onload" occasion has let go), before returning control to your test or script.
    Code line 7: In this line, we are finding the element of the textbox where the "email" has to be written.
    Code line 8: Now we are sending the values to the email section
    Code line 9: Same for the password
    Code line 10: Sending values to the password section
    Code line 11: element.send_keys(Keys.RETURN) is used to press enter after the values are inserted
    Code line 12: close
    
"""





#   https://www.guru99.com/selenium-python.html


##########################################################################################




"""


EXAMPLE 2: Login into Facebook & Check Title

In this example,

    We will open a login page.
    Fill the required field "username" and "password".
    Check Page Title
    
    
"""



 from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox 
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("YOUR EMAILID")
password.send_keys("YOUR PASSWORD")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Facebook"





"""

Explanation of the code:

    Code line 1-2: Import selenium packages
    Code line 4: Initialize Firefox by creating an object
    Code line 6: Get login page (Facebook)
    Code line 8-10: Fetch username, password input boxes and submit button.
    Code line 11-12: Enter data into username and password input boxes
    Code line 14: Click on the "Submit" button
    Code line 15: Create wait object with a timeout of 5 sec.
    Code line 16: Capturing the title from "browser" Object.
    Code Line 17: Testing the captured title string with "Facebook"

"""

