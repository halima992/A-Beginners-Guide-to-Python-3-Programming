# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:07:50 2021

@author: Halima
"""

# =============================================================================
# Exercise1
# Write a program that can find the factorial of any given number. For example, find 
# the factorial of the number 5 (often written as 5!) which is 1 *2* 3* 4* 5 and equals 120. 
# The factorial is not defined for negative numbers and the factorial of Zero is 1;
# that is 0! = 1.
# Your program should take as input an integer from the user (you can reuse your
# logic from the last chapter to verify that 
# they have entered a positive integer value using isnumeric()). 
# You should
# 1. If the number is less than Zero return with an error message. 
# 2. Check to see if the number is Zero—if it is then the answer is 1—print this out. 
# 3. Otherwise use a loop to generate the result and print it out.
# =============================================================================



num = input("please Enter a number:")
factorial = 1 
if num.isnumeric():
    number= int(num)
    if number < 0:
        print('error!')
    elif number == 0:
        print('0! = 1')
    else:
        for i in range(1,number+1):
            factorial = factorial * i
        format_string = "{0}! = {1}" 
        print(format_string.format(number,factorial ))
            
else:
    print('This input is not numarical number')
