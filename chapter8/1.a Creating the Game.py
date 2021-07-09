# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:24:47 2021

@author: Halima
"""

# =============================================================================
# • The program randomly selects a number between 1 and 10. 
# • It will then ask the player to enter their guess. 
# • It will then check to see if that number is the same as the one the computer randomly generated; 
# if it is then the player has won.
# • If the player’s guess is not the same, then it will check to see if the number is higher or lower than the guess 
# and tell the player.
# • The player will have 4 goes to guess the number correctly; 
# if they don’t guess the number within this number of attempts, 
# then they will be informed that they have lost the game and will be told what the actual number was.
# =============================================================================

import random 
print('Welcome to the number guess game')
# Initialise the number to be guessed 
number_to_guess = random.randint(1,10)

# Initialise the number of tries the player has made 
count_number_of_tries = 1

# Obtain their initial guess 
guess = int(input('Please guess a number between 1 and 10: ')) 

while number_to_guess != guess: 
    print('Sorry wrong number')
    # Check to see they have not exceeded the maximum 
    # number of attempts if so break out of loop otherwise
    # give the user come feedback 
    if count_number_of_tries == 4: 
        break
    elif guess < number_to_guess: 
        print('Your guess was lower than the number')
    else: 
        print('Your guess was higher than the number')
        
    # Obtain their next guess and increment number of attempts 
    guess = int(input('Please guess again: ')) 
    count_number_of_tries += 1
    
# Check to see if they did guess the correct number 
if number_to_guess == guess: 
    print('Well done you won!') 
    print('You took', count_number_of_tries , 'goes to complete the game') 
else:
    print("Sorry - you loose") 
    print('The number you needed to guess was', number_to_guess)
    print('Game Over')