"""
Code Challenge
  Name: 
    Posting of Data
  Filename: 
    httpbin.py
  Problem Statement:
      Create a client REST API that sends and receives some information from the Server by calling server's REST API.
      You are expected to create two functions each for Sending and Receiving data.
      You need to make two api calls, one with POST method for sending data and the other with GET method to receive data
      All the communication i.e. sending and receiving of data with the server has to be in JSON format

  Hint:
    Host: httpbin.org
    Port :  80
    Protocol : POST
    URI : /post
    Content-Length: 32 

    firstname=Chris&language=English
"""

import json
import requests

Host = "http://httpbin.org/post"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )

def get_method():
    response = requests.get("http://httpbin.org/get?firstname=Dev&language=English")
    return response

print (get_method().text)