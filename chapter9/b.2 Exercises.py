# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:29:00 2021

@author: Halima
"""

def is_prime(n,i=2):
    if n <= 2:
        if n==2:
            return True
        else:
            return False
    if n%i==0:
        return False
    if i*i > n:
        return True
    return is_prime(n,i+1)


print('is_prime(3):', is_prime(3)) # True 
print('is_prime(7):', is_prime(7)) # True 
print('is_prime(9):', is_prime(9)) # False 
print('is_prime(31):', is_prime(31)) # True

for count in range(0,1):
    print('hi')
    