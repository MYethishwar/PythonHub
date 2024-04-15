#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_of_letters= int(input("How many letters would you like in your password?\n")) 
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

##selects random letters from letters list according to the user input.
selected_letters = random.sample(letters,number_of_letters)
shuffled_letters = random.shuffle(selected_letters)
shuffle_letters_string = ''.join(selected_letters)


#selects random numbers from numbers list according to the user input.
selected_numbers = random.sample(numbers,number_of_numbers)
shuffled_numbers = random.shuffle(selected_numbers)
shuffled__numbers_string = ''.join(selected_numbers)


#selects random symbols from symbols list according to the user input.
selected_symbols = random.sample(symbols,number_of_symbols)
shuffled_symbols = random.shuffle(selected_symbols)
shuffled_symbols_string= ''.join(selected_symbols)

concatenated_password = shuffle_letters_string + shuffled__numbers_string + shuffled_symbols_string
final_password =[]
for item in concatenated_password:
    final_password.append(item)
final_password_shuffle = random.shuffle(final_password)
pypassword = ''.join(final_password)
print(f"Here is your Password created by Yethishwar code: {pypassword}")