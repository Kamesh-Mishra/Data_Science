
"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
import numpy as np

inp = "6 9 2 3 5 8 1 5 4"
inpp = inp.split()

num = np.array(inpp,dtype="int")


#print(num)
print(num.reshape(3,3))
