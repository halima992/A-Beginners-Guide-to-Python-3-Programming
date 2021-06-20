# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:21:23 2021

@author: Halima
"""

# =============================================================================
# The Use of elif
# =============================================================================
savings = float(input("Enter how much you have in savings: ")) 
if savings == 0:
    print("sorry no saving")
elif savings < 500:
    print('Well done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome Sir!')
else:
    print('Thank you')  
# =============================================================================
# Nesting If Statements
# =============================================================================

snowing = True 
temp = -1 
if temp < 0:
    print('It is freezing')
    if snowing:
        print('Put on boots')
    print('Time for Hot Chocolate')
print('Bye')

# =============================================================================
# If Expressions
# =============================================================================

age = 25
status = None
if age > 12 and age < 20:
    status = 'teenager'
else:
    status = 'not teenager'
age = 14
status = ('teenager' if age > 12 and age < 20 else 'not teenager') #bbreviation
print(status)
    