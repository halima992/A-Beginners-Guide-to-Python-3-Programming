# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:46:00 2021

@author: Halima
"""
# =============================================================================
# # Integer Operations
# =============================================================================
home = 10 
away = 15
print(home + away) 
print(type(home + away))
print(10 * 4) 
print(type(10*4))
goals_for = 10 
goals_against = 7 
print(goals_for - goals_against) 
print(type(goals_for - goals_against))
print(100 / 20) 
print(type(100 / 20))  #become float
res1 = 3//2 # // return integer type without number after comma
print(res1)
print(type(res1))
print('Modulus division 4 % 2:', 4 % 2) #return remainder
print('Modulus division 3 % 2:', 3 % 2)

# =============================================================================
# # Negative Number Integer Division
# =============================================================================
print('True division 3/2:', 3 / 2) 
print('True division 3//2:', -3 / 2) 
print('Integer division 3//2:', 3 // 2)  # print 1
print('Integer division 3//2:', -3 // 2) # print -2

# =============================================================================
# Floating Point Number Operators
# print another floating number
# =============================================================================

print(2.3 + 1.5) 
print(1.5 / 2.3) 
print(1.5 * 2.3) 
print(2.3 - 1.5) 
print(1.5 - 2.3)

# =============================================================================
# Integers and Floating Point Operations
# operation  involves integers and floating numbers will produce a floating number
# =============================================================================

i = 3 * 0.1 
print(i)

# =============================================================================
# Complex Number Operators
# using operators such as multiply, add, subtract and divide with complex numbers.
# =============================================================================

c1 = 1j 
c2 = 2j
c3 = c1 * c2 
print(c3)