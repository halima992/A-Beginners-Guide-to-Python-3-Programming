# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:59:39 2021

@author: Halima
"""

# =============================================================================
# The aim of this exercise is to write a small program to test if an integer is positive 
# or negative. Your program should:
# 1. Prompt the user to input a number (use the input() function).
#  You can assume that the input will be some sort of number.
# 2. Convert the string into an integer using the int() function. 
# 3. Now check whether the integer is a positive number or a negative number. 
# 4. You could also add a test to see if the number is Zero.
# =============================================================================

number = int(input('please enter numaric value:'))

if number > 0:
    print('the valus is positive')
elif number < 0:
    print('the valus is negative')
else:
    print('the valus is zero')
    
# =============================================================================
# Test if a Number Is Odd or Even
# The exercises requires you to write a program to take input from the user and 
# determine if the number is odd or even. Again you can assume that the user will 
# enter a valid integer number. 
# Print out a message to the user to let them know the result. 
# To test if a number is even you can use
# (num % 2) == 0 
# Which will return True if the number is even (note the brackets are optional but
# make it easier to read).
#     
# =============================================================================

number = int(input('please enter numaric value:'))

status = ('even' if number % 2 == 0 else 'odd')
print(status)  

# =============================================================================
# In this exercise you should return to the kilometres to miles converter you wrote in 
# the last chapter. We will add several new tests to your program:
# 1. Modify your program such that it verify that the user has entered a positive 
#   distance (i.e. they cannot enter a negative number).
# 2. Now modify your program to verify that the input is a number; if it is not a number 
# then do nothing; otherwise convert the distance to miles.
# To check to see if a string contains only digits use the method isnumeric()
# for example '42'.isnumeric(); which returns True if the string only contains numbers. 
# Note this method only works for positive integers; but this is sufficient for this example.
# =============================================================================

distance_in_killometers = input("please Enter the distance in Kilometres:")
if distance_in_killometers.isnumeric():
    distance_in_killometers = int(distance_in_killometers)
    if (distance_in_killometers>=0):
        distance_in_miles = distance_in_killometers/0.6214
        format_string = "the distance  = {0} miles"  
        print(format_string.format(distance_in_miles))
        
    
    