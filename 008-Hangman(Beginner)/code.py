import random   
import os
from Animal_Names import word_list
from Ascii_Art import logo,stages


#Clears the console screen.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)


#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print("The Chosen Word is a animal name.")
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print(f"You've already guessed --> {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
            print(f"The Animal name is: {chosen_word}")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Won.")
    print(stages[lives])
