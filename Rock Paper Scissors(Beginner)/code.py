import random

#ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
print("What do you choose print 0 for Rock, 1 for Paper, 2 for Scissors.")

user_input = int(input())

#Displays User's choice.
print(game_images[user_input])

#Check is the User's input is valid.
if user_input >= 3:
    print("You typed an invalid number.You Lose!")

#Generate Computers Choice.
computer_input = random.randint(0,2)

#Display computers's choice.
print(game_images[computer_input])

#Main Logic - Decision making.
if (user_input == 0 and computer_input == 2) or (user_input == 1 and computer_input == 0)or (user_input == 2 and computer_input == 1):
    print("You Won")
elif user_input == computer_input:
    print("Draw")
else:
    print("You Lose")
    
