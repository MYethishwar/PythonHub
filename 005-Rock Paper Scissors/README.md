# Rock Paper Scissors Game

## Overview

This Python code simulates a game of Rock, Paper, Scissors where the user competes against the computer.

## Topics Covered

1. **User Input and Display**
   - *Description*: Prompting the user to choose Rock, Paper, or Scissors and displaying their choice.
     ```python
     print("What do you choose? Print 0 for Rock, 1 for Paper, 2 for Scissors.")
     user_input = int(input())
     print(game_images[user_input])
     ```

2. **Check for Valid Input**
   - *Description*: Ensuring the user's input is within the valid range.
     ```python
     if user_input >= 3:
         print("You typed an invalid number. You Lose!")
     ```

3. **Generate Computer's Choice and Display**
   - *Description*: Randomly selecting Rock, Paper, or Scissors for the computer and displaying its choice.
     ```python
     computer_input = random.randint(0, 2)
     print(game_images[computer_input])
     ```

4. **Main Logic - Decision Making**
   - *Description*: Determining the outcome of the game based on the choices made by the user and the computer.
     ```python
     if (user_input == 0 and computer_input == 2) or (user_input == 1 and computer_input == 0) or (user_input == 2 and computer_input == 1):
         print("You Won")
     elif user_input == computer_input:
         print("Draw")
     else:
         print("You Lose")
     ```

