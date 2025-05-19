#Basic level program consists of 2 functions encrypt and decrypt. The user must give the input accordingly otherwise it will give error.
from Ascii_Art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text,shift):
    encrypted_word = ""
    for item in text:
        current_position = alphabet.index(item)
        new_position = (current_position + shift)
        encrypted_word = encrypted_word + alphabet[new_position]
    print(f"The encoded text is {encrypted_word}")
    
def decrypt(text,shift):
    decrypted_word = ""
    for item in text:
        currrent_position = alphabet.index(item)
        new_position = (currrent_position - shift)
        decrypted_word += alphabet[new_position]
    print(f"The decoded text is {decrypted_word}")
    

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
      encrypt(text,shift)  
    elif direction == "decode":
      decrypt(text,shift)
    else:
      print("Please choose a correct option(encode/decode)")
    decision = input("Type 'Yes' if you want to go again. Otherwise type 'No'").lower()
    if decision == "no":
        should_continue = False
        print("Goodbye")
