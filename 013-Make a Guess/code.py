import random
import os
from Ascii_Art import logo

def clear_screen():
    """Clears the console screen"""
    if os.name == 'nt':
        _ = os.system('cls')


def check_the_conditions(attempts,rn):
    """Checks the conditins and print whether the guess is Low or High"""
    to_continue = True
    while 0 < attempts and to_continue:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a Guess: "))
        if user_guess < rn:
            print("Too Low")
            attempts -= 1
        elif user_guess > 100:
            attempts -= 1
            print("OutofBound! Please choose a number between 1 and 100")
        elif user_guess > rn:
            print("Too High")
            attempts -= 1
        else:
            to_continue = False
            print(f"You Got it! The answer was {rn}")
    else:
        print("You've run out of guesses, you lose.")
        print(f"The number is {rn}")
                
                
def easy_level(rn): 
    """Switches to Easy level Attempts:- 5"""  
    attempts = 10
    check_the_conditions(attempts,rn)
    
def hard_level(rn):
    """Switches to Hard level Attempts:- 10"""
    attempts  = 5
    check_the_conditions(attempts,rn)
    
play_again = True
while play_again:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm Thinking of a number between 1 and 100.")
    random_number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        easy_level(random_number)
    elif difficulty == 'hard':
        hard_level(random_number)
    else:
        print("You choose an incorrect option, Please Try Again!")
    want_to_play = input("Do you want to play Again Type 'yes' or 'no': ")
    if want_to_play == "yes":
        play_again = True
        clear_screen()
    else:
        print("Thank you for playing the game Program written by Yethishwar.\nYour participation is appreciated!")
        play_again = False