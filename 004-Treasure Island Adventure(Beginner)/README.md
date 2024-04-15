# Treasure Island Adventure

## Overview

This Python code guides the user through an adventure on Treasure Island, where they make decisions to reach the treasure.

## Topics Covered (If, else, elif)

1. **Displaying ASCII Art**
   - *Description*: The code prints ASCII art representing a decorative header for the game.
   - ```python
     print('''
     *******************************************************************************
               |                   |                  |                     |
      _________|________________.=""_;=.______________|_____________________|_______
     |                   |  ,-"_,=""     `"=.|                  |
     |___________________|__"=._o`"-._        `"=.______________|___________________
               |                `"=._o`"=._      _`"=._                     |
      _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
     |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
     |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
               |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
      _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
     |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
     |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
     ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
     /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
     ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
     /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
     ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
     /______/______/______/______/______/______/______/______/______/______/_____ /
     *******************************************************************************
     ''')
     ```

2. **Welcoming Message**
   - *Description*: The code displays a welcoming message for the user.
   - ```python
     print("Welcome to Treasure Island.")
     ```

3. **Mission Overview**
   - *Description*: The code provides an overview of the user's mission.
   - ```python
     print("Your mission is to find the treasure.")
     ```

4. **Choosing Direction**
   - *Description*: The code prompts the user to choose a direction (left or right) at the crossroad.
   - ```python
     print("You are at a Cross Road. Where do you want to go Left or Right? ")
     decision1 = input().lower()
     ```

5. **Handling Left Path**
   - *Description*: The code guides the user through the left path decision.
   - ```python
     if decision1 == "left":
         # Code for handling the left path decision
     ```

6. **Handling Right Path**
   - *Description*: The code guides the user through the right path decision.
   - ```python
     else:
         # Code for handling the right path decision
     ```

7. **Handling Boat Decision**
   - *Description*: The code guides the user through the decision to take a boat.
   - ```python
     if decision2 == "boat":
         # Code for handling the decision to take a boat
     ```

8. **Handling Rocky Path Decision**
   - *Description*: The code guides the user through the decision to take the rocky path.
   - ```python
     if decision3 == "rocky":
         # Code for handling the decision to take the rocky path
     ```

9. **Handling House Door Decision**
   - *Description*: The code guides the user through the decision of choosing a door in the house.
   - ```python
     if decision4 == "yellow":
         # Code for handling the decision of choosing the yellow door
     elif decision4 == "red":
         # Code for handling the decision of choosing the red door
     elif decision4 == "blue":
         # Code for handling the decision of choosing the blue door
     else:
         # Default case
     ```
