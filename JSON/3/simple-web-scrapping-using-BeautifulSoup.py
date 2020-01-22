import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

page.status_code

page.content


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'lxml')

soup



print(soup.prettify())


soup.children         #list generator , so we have to call it in list

list(soup.children)


list(soup.children)[0]


list(soup.children)[1]



# To see the type
[type(item) for item in list(soup.children)]

html = list(soup.children)[1]

list(html.children)



body = body = list(html.children)[3]

body



list(body.children)



list(body.children)[1]

p = list(body.children)[1]
p.get_text()       ## We can use the get_text method to extract all of the text inside the tag




"""
What we did above was useful for figuring out how to navigate 
a page, but it took a lot of commands to do something fairly simple. 
If we want to extract a single tag, we can instead use the find_all method, which 
will find all the instances of a tag on a page
"""

soup = BeautifulSoup(page.content, 'lxml')
soup.find_all('p')



#   Note it returns the list so we use list indexing

soup.find_all('p')[0]



soup.find_all('p')[0].get_text()



## we can also use find()

soup.find('p')


soup.find('p').get_text()









