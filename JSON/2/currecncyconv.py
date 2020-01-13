
"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=07ca862e0b339dd56245
    or
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""


import requests

url = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=07ca862e0b339dd56245"

response = requests.get("http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=07ca862e0b339dd56245")

k = response.json()

print('Currency Converted Convert  from USD to INR >> ',k['USD_INR'])