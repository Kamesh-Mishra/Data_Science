# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:26:51 2020

@author: USER
"""


# test0.py
from prime import is_prime

def test_prime(n,expected):
  if is_prime(n) != expected :
    print(f"ERROR on is_prime{n}, expected {expected}")
  else:
    print("PASSED")
    
"""    
test_prime(1,False)
test_prime(2,True)
test_prime(8,False)
test_prime(11,True)
test_prime(25,False)
test_prime(28,False)
"""

