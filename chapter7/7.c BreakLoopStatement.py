# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:53:05 2021

@author: Halima
"""
print('Only print code if all iterations completed') 
num = int(input('Enter a number to check for: '))
for i in range(0,6):
    if i == num:
        break
    print(i,' ', end=' ')
print(' ')
print('Done')