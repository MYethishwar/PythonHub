# Caesar Cipher

## Introduction
The Caesar Cipher is one of the simplest and oldest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down the alphabet.

## How it Works
Let's say we want to encrypt the message "HELLO" using a Caesar Cipher with a shift of 3:

- H becomes K
- E becomes H
- L becomes O
- L becomes O
- O becomes R

So, "HELLO" would be encrypted as "KHOOR".

## Program written in Three Levels
### BasicHelper
The BasicHelper program provides a simple implementation of the Caesar Cipher. It prompts the user to enter a message and a shift value, then outputs the encrypted message.

### Moderator
The Moderator program offers a more customizable version of the Caesar Cipher. It allows the user to choose between encryption and decryption, specify the message and shift value, and provides options for handling special characters.

### Challenger
The Challenger program is an advanced implementation of the Caesar Cipher. It not only encrypts and decrypts messages but also includes additional features such as handling uppercase and lowercase letters separately, and providing options for brute-force 
## Sample Output

```plaintext
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88

Type 'encode' to encrypt, type 'decode' to decrypt:
enCODE 
Type your message:
hello
Type the shift number:
5
The encoded text is mjqqt
Type 'Yes' if you want to go again. Otherwise type 'No'
YES
Type 'encode' to encrypt, type 'decode' to decrypt:
decodE
Type your message:
mjqqt
Type the shift number:
5
The decoded text is hello
Type 'Yes' if you want to go again. Otherwise type 'No'
NO
Goodbye