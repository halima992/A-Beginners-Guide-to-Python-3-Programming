# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:39:05 2021

@author: Halima
"""
#--------------------integer number--------------------
x = 1
print(x)
print(type(x))

#convert another type into an integer using the int()
x = '100'
print(type(x))
x = int(x)
print(type(x))

age = int(input('Please enter your age:'))
print(type(age)) 
print(age)
#------------------------------------------------------

#---------------------float number---------------------
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))

#convert another type into an floatfloat using the float()
int_vlue = 1
string_vlue = '1.5'
float_value = float(int_vlue)
print('int value as a float:', float_value)
print(type(float_value))
float_value = float(string_vlue)
print('string value as a float:', float_value)
print(type(float_value))
#------------------------------------------------------

#----------converting input string into float----------
exchange_rate = float(input(
    "Please enter the exchange rate to use: "))
print(exchange_rate) 
print(type(exchange_rate))
#------------------------------------------------------

#-------------------complex  numbers-------------------
c1 = 1j
c2 = 2j
print('c1:', c1,', c2:', c2)
print(type(c1))
print(c1.real)
print(c1.imag)
#------------------------------------------------------


