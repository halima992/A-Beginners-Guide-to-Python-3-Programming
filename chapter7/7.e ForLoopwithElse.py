# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:48:31 2021

@author: Halima
"""
print('Only print code if all iterations completed') 
num = int(input('Enter a number to check for: '))
for i in range(0,6):
    if i == num:
        break
    print(i,' ', end=' ')
else:
    print(' ')
    print('All iterations successful')