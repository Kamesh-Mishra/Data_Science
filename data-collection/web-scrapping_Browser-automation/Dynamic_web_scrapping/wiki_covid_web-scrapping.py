# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:54:55 2020

@author: USER
"""

import pandas as pd 
from selenium import webdriver
# from bs4 import BeautifulSoup
# import requests

driver = webdriver.Firefox(executable_path="E:\geckodriver\geckodriver.exe")

url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/India_medical_cases_by_state_and_union_territory"

# open url in browser
driver.get(url)

table = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[3]/table')

thead = table.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[3]/table/thead")

A = []

for ind,tr in enumerate(thead.find_elements_by_tag_name('tr')):
    th = tr.find_elements_by_tag_name('th')
    if ind == 1:
        A.append(th[0].text.strip())
        A.append(th[1].text.strip())
        A.append(th[2].text.strip())
        A.append(th[3].text.strip())
        A.append(th[4].text.strip())
        
        
        
tbody = table.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[3]/table/tbody")

B = []
C = []
D = []
E = []
F = []


for tag in tbody.find_elements_by_tag_name('tr')[:-2]:
    
    th = tag.find_element_by_tag_name('th')
    B.append(th.text.strip())
    
    td = tag.find_elements_by_tag_name('td')
    C.append(td[0].text.strip())
    D.append(td[1].text.strip())
    E.append(td[2].text.strip())
    F.append(td[3].text.strip())    

print(B)
print(C)
print(D)
print(E)
print(F)

driver.quit()
    
from collections import OrderedDict

col_data = OrderedDict(zip(A,[B,C,D,E,F]))

data = pd.DataFrame(data)
print(data)



