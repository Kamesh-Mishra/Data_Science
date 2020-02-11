from selenium import webdriver

from  time import sleep


username = input("Enter username : ")

pw  = input("Enter password : ")

# browser = webdriver.Firefox(executable_path="E:/geckodriver/geckodriver.exe")


class InstaBot:
     def __init__(self, username, pw):
         self.driver = webdriver.Firefox(executable_path="E:/geckodriver/geckodriver.exe")
         self.driver.get("https://instagram.com")
         sleep(5)
         
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a").click()
         sleep(5)
         self.driver.find_element_by_name("username").send_keys(username)
         
         self.driver.find_element_by_name("password").send_keys(pw)

        
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button").click()

         sleep(5)
         
         
        
InstaBot(username, pw)

