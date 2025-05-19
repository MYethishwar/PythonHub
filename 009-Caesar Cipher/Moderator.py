
from Ascii_Art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text,shift,direction):
    final_result = ""
    for item in text:

        current_position = alphabet.index(item)
        if direction == "encode":
            new_position = (current_position + shift)
        elif direction == "decode":
            new_position = (current_position - shift)
        final_result = final_result + alphabet[new_position]
    print(f"The {direction}d text is {final_result}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    decision = input("Type 'Yes' if you want to go again. Otherwise type 'No'").lower()
    if decision == "no":
        should_continue = False
        print("Goodbye")
 

