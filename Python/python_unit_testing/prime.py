# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:32:15 2020

@author: USER
"""



import math
def is_prime(n):
  """Determine if a non-negative integer is prime"""
  if n < 2 :
    return False

  # OFF BY ONE Error, solution is to add +1  
  # for i in range (2, int(math.sqrt(n)) + 1 ):
  for i in range (2, int(math.sqrt(n))):
    if n % i == 0 :
      return False
  return True


# list of prime numbers

# is_prime WILL return TRUE  
# 2, 3, 5, 7, 11, 13, 17, 19, 23
  
# is_prime WILL return FALSE  
# 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28

is_prime(1)   # SUCCESS
is_prime(2)   # SUCCESS
is_prime(8)   # FAIL   
is_prime(11)  # SUCCESS
is_prime(25)  # FAIL 
is_prime(28)  # SUCCESS