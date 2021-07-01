# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:55:51 2021

@author: Halima
"""
import random
MIN = 1
MAX = 6
roll_again = 'y'

while roll_again == 'y':
    print('Rolling the dices...') 
    print('The values are....')
    dic1 = random.randint(MIN, MAX)
    print(dic1)
    dic2 = random.randint(MIN, MAX)
    print(dic2)
    roll_again = input('Roll the dices again? (y / n): ')