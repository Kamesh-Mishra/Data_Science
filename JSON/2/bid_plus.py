
"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""



from  selenium import webdriver
#from time import sleep
# from bs4 import BeautifulSoup as BS


A = []

B = []

C = []

D = []

E = []

F = []

for i in range(1,5):
    url = "https://bidplus.gem.gov.in/bidlists?bidlists&page_no="+str(i)
    
    browser = webdriver.Firefox(executable_path="E:/geckodriver/geckodriver.exe")
    
    
    
    browser.get(url)
    
    
    all_data = browser.find_element_by_id('pagi_content')    
    
    
    all_data = all_data.find_elements_by_class_name('border block')
    
    
    print(all_data)
    
    
            
    var1 = all_data.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/p[1]/a').text

    var2 = all_data.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/p[1]/span').text
    
    
    
    var3 = all_data.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/p[2]/span').text
    var4 = all_data.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/p[2]').text
    var5 = all_data.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[4]/p[1]/span').text
    var6 = all_data.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[4]/p[2]/span').text
    
    print(var1, var2, var3 , var4 , var5, var6 , sep= "\n")
    
     
    
        
        
    
    A.append(var1.strip())
    
    B.append(var2.strip())
    
    C.append(var3.strip())
    
    D.append(var4.strip())
    
    E.append(var5.strip())
    
    F.append(var6.strip())
    
    
    col = ["BID NO: ", "Item(s): ", "Quantity Required: ", "Department Name And Address: ", "Start Date: ", "End Date: "]
    
    from collections import OrderedDict
    
    import pandas as pd
    
    col_data = OrderedDict(zip(col,[A,B,C,D,E,F]))
    
    
    df = pd.DataFrame(col_data) 
    print(df)
    # df.to_csv("sitedata.csv")
    browser.quit()