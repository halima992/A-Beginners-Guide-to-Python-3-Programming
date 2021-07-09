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
    if number == 0:
        print('0! = 1')
    else:
        for i in range(1,number+1):
            factorial = factorial * i
        format_string = "{0}! = {1}" 
        print(format_string.format(number,factorial ))
            
else:
    print('This input is not numarical number')

# =============================================================================
# Exercise2
# A Prime Number is a positive whole number, greater than 1,
# that has no other divisors except the number 1 and the number itself. 
# That is, it can only be divided by itself and the number 1, 
# for example thenumbers 2, 3, 5 and 7 are prime numbers as they cannot be divided by 
# any other whole number. However, the numbers 4 and 6 are not because they can both be divided by the number 2 
# in addition the number 6 can also be divided by the number 3. 
# You should write a program to calculate prime number starting from 1 up to the
# value input by the user. 
# If the user inputs a number below 2, print an error message. 
# For any number greater than 2 loop for each integer from 2 to that number and
# determine if it can be divided by another number 
# (you will probably need two for loops for this; one nested inside the other). 
# For each number that cannot be divided by any other number (that is its a prime number) 
# print it out.
# =============================================================================

num = input("please Enter a prime number:")
if num.isnumeric():
    number= int(num)
    if number < 2:
        print('error!')
    else:
        
        for i in range(1,number+1):
            flag = 0
            for j in range(2, int(i/2)):
                if i%j == 0:
                    flag=flag+1
                    break
            if flag == 0:
                print(i, end = ' ')
    

