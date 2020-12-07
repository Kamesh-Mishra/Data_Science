

"""
Code Challenge

Download the image from the URL and store in a file

https://imgs.xkcd.com/comics/python.png

"""
import requests

url = "https://imgs.xkcd.com/comics/python.png"

response = requests.get(url)

if response.status_code == 200:
    with open("python.png",'wb') as f:
        f.write(response.content)