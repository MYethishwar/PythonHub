
from data import data 
from Ascii_Art import logo,vs
import random
import os

#Clears the console screen whenever requires.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

#Checks which person has more followers and returns True or False.
def which_is_greater(count_A,count_B,decision):
    if count_A >  count_B:
        return decision == "a"
    else:
        return decision == "b"
    
score = 0
to_continue = True
random_person2 = random.choice(data)

#Repeat the loop until user chose an incorrect one.s
while to_continue:
    print(logo)
    random_person1 = random_person2
    random_person2 = random.choice(data)
    
    if random_person1 == random_person2:
        random_person2 = random.choice(data)

    # Fomrating the data inside the dictionary.
    person1 = (f"Compare A: {random_person1['name']}, a {random_person1['description']}, from {random_person1['country']}.")
    person2 = (f"Against B: {random_person2['name']}, a {random_person2['description']}, from {random_person2['country']}.")
    print(person1)
    print(vs)
    print(person2)
    user_desicion = input("Who has more followers? Type 'A' or 'B': ").lower()
    person1_followers = random_person1['follower_count']
    person2_followers = random_person2['follower_count']
    is_correct = which_is_greater(person1_followers,person2_followers,user_desicion)
    clear()
    print(logo)
    if is_correct:  
        score += 1
        print(f"You,re right! Current Score: {score}")
    else:   
        to_continue = False
        print(f"Sorry! that's wrong Final Score: {score}")