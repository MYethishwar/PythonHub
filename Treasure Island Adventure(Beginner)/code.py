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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You are at a Cross Road. Where do you want to go Left or Right? ")
decision1 = input()
decision1 = decision1.lower()

if decision1 == "left":
    print("You came to a lake. There is an island in the middle of the lake. Do you want to wait for a boat or swim?")
    decision2 = input()
    decision2 = decision2.lower()
    
    if decision2 == "boat":
        print("You arrived at the island safely.\nThere is a mountain. Which path do you prefer for climbing the mountain: rocky or grassy?")
        decision3 = input()
        decision3 = decision3.lower()
        
        if decision3 == "rocky":
            print("You successfully reached the top of the mountain.\nThere is a house with 3 doors: one red, one blue, one yellow. Which one do you choose? ")
            decision4 = input()
            decision4 = decision4.lower()
            
            if decision4 == "yellow":
                print("Congratulations. You won the match!")
            elif decision4 == "red":
                print("'Burned by Fire'. Game Over!")
            elif decision4 == "blue":
                print("'Eaten by Beasts'. Game Over!")
            else:
                print("Game Over")   
                 
        else:
            print("'You encountered a snake'. Game Over!")
            
    else:
        print("'Attacked by Crocodile'. Game Over!")   
        
else:
    print("'Fall in a Hole'. Game Over")
