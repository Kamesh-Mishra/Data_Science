

"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi
"""


import pandas as pd
from selenium import webdriver


url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"


driver = webdriver.Firefox(executable_path="E:\geckodriver\geckodriver.exe")

# Opening the submission url
driver.get(url)


all_tables   =  driver.find_element_by_tag_name('tbody')


driver.quit()
#df = pd.DataFrame(all_tables)

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]


for row in all_tables.find_elements_by_tag_name('tr'):
    
    cells = row.find_elements_by_tag_name('td')
    
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        



from collections import OrderedDict

col_name = ["Pos","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

df = pd.DataFrame(col_data) 
print(df)




import sqlite3
conn = sqlite3.connect ( 'ranking.db' )
c = conn.cursor()


df.to_sql("rankingselenium", con=conn, if_exists = 'replace', index=False)

c.execute("SELECT * FROM rankingselenium")

c.fetchall()

