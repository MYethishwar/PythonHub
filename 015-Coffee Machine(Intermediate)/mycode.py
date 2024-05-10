from data import menu, resources
import os
# ☕
# ₹
def is_transaction_successfull(m_value,item):
    """returns true if user entered sufficient money as required to make a drink"""
    if m_value >= item['cost']:
        change = m_value - item['cost']
        return change, True
    else:
        return 0,False
def deduct_resources(i):
    ingredients = i['ingredients']
    resources['water'] -= ingredients['water']
    resources['milk'] -= ingredients['milk']
    resources['coffee'] -= ingredients['coffee']


def process_coins():
    """Returns the total calculated amount From coins inserted"""
    print("Please insert Coins")
    one = int(input("How many ONE rupee coins?"))
    two = int(input("How many TWO rupee coins?"))
    five = int(input("How many FIVE rupee coins?"))
    ten = int(input("How many TEN rupee coins?"))
    total_value = ((one * 1) + (two * 2) + (five * 5) + (ten * 10))
    return total_value

def check_resources(item):
    """returns true if resources available or false if it is not available"""
    ingredients = item['ingredients']
    if (resources['water'] <  ingredients['water']):
        return "water",False
    elif (resources['milk'] <  ingredients['milk']):
        return "milk",False
    elif (resources['coffee'] <  ingredients['coffee']):
        return "coffee",False
    else:
        return "available",True

def return_report():
    """Returns a report of the present resources"""
    return f"water: {resources['water']}ml\nmilk: {resources['milk']}ml\ncoffee: {resources['coffee']}g\nmoney: ₹{resources['money']}"

machine_active = True
while machine_active == True:
    user_choice = input("Here is your menu👇\nSleepy Owl Coffee - ₹100\nIrani Chai - ₹200\nMasala Chai - ₹300\nWhat would you like?").lower()
    if user_choice == 'off':
        machine_active = False
    elif user_choice == 'report':
        print(f"Here is your report:\n{return_report()}")
    elif ((user_choice == 'masala chai') or ( user_choice == 'irani chai') or (user_choice == 'sleepy owl coffee')):
        item = menu[user_choice]
        is_resources_available = check_resources(item)
        if is_resources_available[1] == True:
            payment = process_coins()
            transaction = is_transaction_successfull(payment, item)
            if transaction[1]:
                resources['money'] += item['cost']
                if transaction[0] != 0:
                    print(f"Here is ₹{transaction[0]} change")
                deduct_resources(item)
                print(f"Here is your {user_choice}☕. ENJOY!")
            else:
                print("Sorry that's not enough money. Money refunded!")
        else:
            print(f"Sorry there is not enough {is_resources_available[0]}")

    else:
        print("Please select the item which is in the menu Correctly.")



