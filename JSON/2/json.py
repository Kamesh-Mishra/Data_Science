


"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing in human readable format
"""



import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)

jsondata = response.json()

#print(jsondata)

print('coordinates ',jsondata['coord'])

#or

print("lattitude ",jsondata["coord"]['lat'])

print("longitude ",jsondata['coord']['lon'])


print('weather ',jsondata['weather'][0])

print('wind speed ',jsondata['wind']['speed'])


import time
print('sunrise time ',time.ctime(jsondata["sys"]["sunrise"]))


print('sunset time ',time.ctime(jsondata["sys"]["sunset"]))
