# Hangman Game

## Overview

This Python code implements a Hangman game where the player needs to guess a word by entering letters. The game provides a limited number of attempts to guess the word correctly. If the player exceeds the allowed number of attempts, they lose the game.

## Topics Covered.

1. **Imports**
   - *Description*: The script imports necessary modules and functions.
   - 
     ```python
     import random   
     import os
     from Animal_Names import word_list
     from Ascii_Art import logo, stages
     ```

2. **Clearing the Screen**
   - *Description*: The script defines a function to clear the console screen.
   - 
     ```python
     def clear():
         os.system('cls' if os.name == 'nt' else 'clear')
     ```

3. **Initializing Game Variables**
   - *Description*: The script initializes variables such as the chosen word, word length, and remaining lives.
   - 
     ```python
     end_of_game = False
     chosen_word = random.choice(word_list)
     word_length = len(chosen_word)
     lives = 6
     ```

4. **Main Game Loop**
   - *Description*: The script runs the main game loop where the player guesses letters until they either win or lose the game.
   - 
     ```python
     while not end_of_game:
         # Display current game state
         # Prompt player to guess a letter
         # Check if guessed letter is in the word
         # Update game state accordingly
         # Check if player has won or lost
     ```

5. **Checking Guesses and Updating Display**
   - *Description*: The script checks the player's guessed letter against the chosen word and updates the display accordingly.
   - 
     ```python
     for position in range(word_length):
         letter = chosen_word[position]
         if letter == guess:
             display[position] = letter
     ```

6. **End of Game Conditions**
   - *Description*: The script checks if the player has won or lost the game and prints the appropriate message.
   - 
     ```python
     if "_" not in display:
         end_of_game = True
         print("You Won.")
     if lives == 0:
         end_of_game = True
         print("You Lose")
         print(f"The Animal name is: {chosen_word}")
     ```

7. **Printing Game State**
   - *Description*: The script prints the current state of the Hangman game, including the Hangman figure and the word display.
   - 
     ```python
     print(f"{' '.join(display)}")
     print(stages[lives])
     ```
