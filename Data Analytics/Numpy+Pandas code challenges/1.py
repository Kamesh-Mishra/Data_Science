
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

# extract tables from wikipedia
from pandas.io.html import read_html
import matplotlib.pyplot as plt

page = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
wikitables = read_html(page,  attrs={"class":"wikitable"})
print ("Extracted {num} wikitables".format(num=len(wikitables)))
df = wikitables[0]


dff = df.iloc[:6,[1,4]]
print(dff)


labels = df.iloc[0:6,1]
sizes = df.iloc[0:6,4]
plt.pie(sizes, labels=labels, autopct='%.0f%%')
plt.show()
