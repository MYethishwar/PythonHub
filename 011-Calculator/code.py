from Ascii_Art import logo
import os
def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def Addition(n1,n2):
    return n1+n2
def Multiplication(n1,n2):
    return n1*n2
def Division(n1,n2):
    return n1/n2
def Subtraction(n1,n2):
    return n1-n2

operations = {
    "+":Addition,
    "-":Subtraction,
    "*":Multiplication,
    "/":Division
    }

def calculator():
    """
    Recursive Function performs Basic Arithmatic Operations.
    """
    print(logo)
    num1 = float(input("What's the first number? "))
    for key in operations:
        print(key)
    is_true = True
    while is_true:
        operation_symbol = input("Pick an operation:")
        if operation_symbol not in operations.keys():
            print("Sorry, You entered Invalid Operational Symbol, Please Try Again!")
        else:
            num2 = float(input("What's the next number? "))
            function = operations[operation_symbol]
            answer = function(num1,num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}\n")

            to_continue = input(f"'Y' ---> To calculate with {answer}.\n'N' ---> To start from Starting.\n'E' ---> To exit.\nENTER HERE ---> " ).lower()
        
            if to_continue == "y":
                num1 = answer   
            elif to_continue == "n":
                clear()
                calculator()
            elif to_continue == "e":
                return  "Thank You for using Yethsihwar's Calculator"
            else:
                return "You chose an Invalid Option, Please Try Again!"
            
print(calculator())