# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:58:38 2021

@author: Halima
"""
for i in range (0,10):
    print(i,' ',end=' ')
    if i%2 == 1:
        print()
        continue
    print('hey its an even number')
print('Done')