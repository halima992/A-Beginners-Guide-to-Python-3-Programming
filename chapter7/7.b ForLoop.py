# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:36:42 2021

@author: Halima
"""
# Loop over a set of values in a range
for i in range(0,10):
    print(i, ' ',end=' ')
print()
print('Done')

# Now use values in a range but increment by 2

for i in range(0,10,2):
    print(i, ' ',end=' ')
print()
print('Done')

# Now use an 'anonymous' loop variable 
for _ in range(0,10): 
    print('.', end='')
print()