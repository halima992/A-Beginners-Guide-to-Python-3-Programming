# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:50:36 2021

@author: Halima
"""
# =============================================================================
# 5.11.2 Convert Kilometres to Miles
# The aim of this exercise is to write a program to convert a distance in Kilometres into a distance in miles.
# 1. Take input from the user for a given distance in Kilometres. This can be done using the input() function.
# 2. Convert the value returned by the input() function from a string into an integer using the int() function.
# 3. Now convert this value into miles—this can be done by dividing the kilometres by 0.6214
# 4. Print out a message telling the user what the kilometres are in miles.
# =============================================================================
distance_in_killometers = int(input("please Enter the distance in Kilometres:"))
distance_in_miles = distance_in_killometers/0.6214
format_string = "this distance  = {0} miles"  
print(format_string.format(distance_in_miles))
