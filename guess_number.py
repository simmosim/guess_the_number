#Guess the Number

import random

def is_valid_number(s):
    if s.isdigit() and 1 <= int(s) <= 100: #isdigit returns 
        return True                     #True if there's >= one 
    else:                               #digit in s and they're 
        return False                    #all digits

def user_guess():
    num = random.randint(1, 100)
    guessed_number = False
    guess = input("Guess a number between 1 and 100: ")
    num_guesses = 0
    print("Your guess is {}".format(guess))
    
    while not guessed_number:
        if not is_valid_number(guess):
            guess = input("You need to input a number between 1 and 100: ")
            continue #Goes to next iteration of while loop
        else:        #without going further in THIS iteration
            num_guesses += 1
            guess = int(guess)
            
        if guess < num:
            guess = input("Your guess was too low, IDIOT! Guess again!")
        elif guess > num:
            guess = input("Your guess was too high, STUPID! Guess again!")
        else:
            print("You got it in",num_guesses,"guesses! Well done?")
            again = input("Would you like to play again? (Y or N): ")
            if again.lower() == "y":
                user_guess()
            



#Concepts to keep in mind:

#Random function
#Variables
#Integers
#Input/Output
#Print
#While loops
#If/Else statements


