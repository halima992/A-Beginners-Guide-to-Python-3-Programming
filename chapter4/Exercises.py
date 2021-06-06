# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 22:57:40 2021

@author: Halima
"""

# Exercise 1
some_string = 'Denyse,Marie,Smith,21,London,UK'
some_string = some_string.replace(',', ' ')
print(some_string)

# Exercise 2
first_string = input('Enter the first sentence:')
second_string = input('Enter  the second sentence:')
new_string = (first_string + ' ' + second_string)
print(new_string)

print(len(new_string))

print(new_string.upper())

print(new_string.find('Albus'))