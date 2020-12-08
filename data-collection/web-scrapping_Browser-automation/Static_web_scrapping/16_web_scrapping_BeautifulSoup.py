
# Web Scraping with BeautifulSoup and Requests

# Parsing the content from the website and 
# pulling  the exact information you want
# Introduce to the page for Web Scrapping 

# pip install beautifulsoup4
# pip install lxml
# pip install html5lib

"""
Introduce the concept of basic HTML tags
HTML
  HEAD
    
  HEAD

  BODY
    
  BODY
HTML

"""

from bs4 import BeautifulSoup


# Create simple html files and 
# parse that using bs4 to make the students understand with title, div etc


html_file = open("simple.html")

soup = BeautifulSoup(html_file, "lxml") # html5lib is another parser

print (soup)

print (soup.prettify())

print (soup.title)

print (soup.title.text)

print (soup.div)

print (soup.div.h1.text)

# Crome browser ( use the inspect tool to use the find function )
match = soup.find('div')
print (match)

match = soup.find("div", class_= "footer")
print (match)

print ( match.h2 )
print ( match.h2.text )

print ( match.p )
print ( match.p.text )

for article in soup.find_all("div") :
  headline = article.p.text
  print (headline)


# Give students a challenge to print some information from the HTML pages 




# Reading from the Internet
from bs4 import BeautifulSoup   
import requests

source = requests.get("http://httpbin.org/html").text
print(source)

soup = BeautifulSoup(source,"lxml")

print (soup)

print (soup.prettify())

print (soup.head)
print (soup.head.text)

print (soup.body)

print (soup.body.h1)
print (soup.body.h1.text)


print (soup.body.div)
print (soup.body.div.p)
print (soup.body.div.p.text)



#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
import urllib



#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)         #for urllib library

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='wikitable')

print (right_table)


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())



from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
