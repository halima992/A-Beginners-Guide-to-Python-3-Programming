# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:27:34 2021

@author: Halima
"""
all_ok =  True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

# Boolean type is a sub type of integer
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))

# convert strings into Booleans
status = bool(input('OK to proceed:'))
print(status)
print(type(status))
