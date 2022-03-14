# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:14:36 2021

@author: Halima
"""
def factorial(n):
    if n == 1:
        res = 1
        return res
    else:
        res = n*factorial(n-1)
        return res
    
    
    
print(factorial(4))



output = []
def function(num):
    digits = str(num)
    for i, digit in enumerate(digits):
        if int(digit)!=0:
            index = len(digits)-1-i
            output.append(digit + ('0' * index))
            #output.append(str(num))
    return " + ".join(output)

print(function(70304))