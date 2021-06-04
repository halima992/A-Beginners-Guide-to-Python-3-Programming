# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:14:40 2021

@author: Halima
"""
# String Concatenation
string_1 = 'Good' 
string_2 = " day"
string_3 = string_1 + string_2 
print(string_3) 
print('Hello ' + 'World')

# Length of a String
print(len(string_3))

# Accessing a Character
my_string = 'Hello World' 
print(my_string[4])

# Accessing a Subset of Characters
my_string = 'Hello World' 
print(my_string[4]) # characters at position 4 
print(my_string[1:5]) # from position 1 to 5 
print(my_string[:5]) # from start to position 5 
print(my_string[2:]) # from position 2 to the end

# Repeating Strings
print('*' * 10) 
print('Hi' * 10)

# Splitting Strings
title = 'The Good, The Bad, and the Ugly' 
print('Source string:', title) 
print('Split using a space') 
print(title.split(' ')) 
print('Split using a comma') 
print(title.split(','))

# Counting Strings
my_string = 'Count, the number of     spaces' 
print("my_string.count(' '):", my_string.count(' '))

# Replacing Strings
welcome_message = 'Hello World!' 
print(welcome_message.replace("Hello", "Goodbye"))

# Finding Sub Strings
print('Edward Alun Rawlings'.find('Alun'))
print('Edward John Rawlings'.find('Alun'))

# Converting Other Types into Strings
'''msg = 'Hello Lloyd you are ' + 21 
   print(msg) 
   You will get an error message'''
   
msg = 'Hello Lloyd you are ' + str(21) 
print(msg) 

# Comparing Strings
print('James' == 'James') # prints True 
print('James' == 'John') # prints False 
print('James' != 'John') # prints True
print('James' == 'james') # prints False 

# Other String Operations
some_string = 'Hello World' 
print('Testing a String') 
print('-' * 20) 
print('some_string', some_string) 
print("some_string.startswith('H')", some_string.startswith('H')) 
print("some_string.startswith('h')", some_string.startswith('h')) 
print("some_string.endswith('d')", some_string.endswith('d')) 
print('some_string.istitle()', some_string.istitle()) 
print('some_string.isupper()', some_string.isupper()) 
print('some_string.islower()', some_string.islower()) 
print('some_string.isalpha()', some_string.isalpha())
print('String conversions') 
print('-' * 20) 
print('some_string.upper()', some_string.upper()) 
print('some_string.lower()', some_string.lower()) 
print('some_string.title()', some_string.title()) 
print('some_string.swapcase()', some_string.swapcase()) 
print('String leading, trailing spaces', " xyz ".strip())

