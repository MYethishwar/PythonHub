from Ascii_Art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(initial_text, shift_number, choice):
    result_text = ""
    if choice == "decode":
        shift_number *= -1
    for item in initial_text:
        if item in alphabet:
            current_position = alphabet.index(item)
            new_position = (current_position + shift_number) % 26
            result_text += alphabet[new_position]
        else:
            result_text += item
    print(f"The {choice}d text is {result_text}")
    
print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    decision = input("Type 'Yes' if you want to go again. Otherwise type 'No'\n").lower()
    if decision == "no":
        should_continue = False
        print("Goodbye")




