# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 22:16:26 2021

@author: Halima
"""

format_string = 'Hello {}!'
print(format_string.format('Phoebe'))

# Allows multiple values to populate the string 
name = "Adam" 
age = 20 
print("{} is {} years old".format(name, age))

# Can specify an index for the substitution 
format_string = "Hello {1} {0}, you got {2}%" 
print(format_string.format('Smith', 'Carol', 75))


# Can use named substitutions, order is not significant ---> this one i will used
format_string = "{artist} sang {song} in {year}" 
print(format_string.format(artist='Paloma Faith', song='Guilty', year=2017))

print('|{:25}|'.format('25 characters width'))

# • < Indicates left alignment (the default),
# • > Indicates right alignment, 
# • ^ Indicates centered.

print('|{:<25}|'.format('left aligned')) # The default 
print('|{:>25}|'.format('right aligned')) 
print('|{:^25}|'.format('centered'))

print('{:,}'.format(1234567890)) 
print('{:,}'.format(1234567890.0))