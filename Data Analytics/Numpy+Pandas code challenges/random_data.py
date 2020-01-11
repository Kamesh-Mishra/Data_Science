

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""


import numpy as np

arr=np.random.randint(5,15, size=40)
print (arr)


from scipy import stats
print("most frequent value: ", stats.mode(arr))
