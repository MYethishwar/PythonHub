import os
def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
from Ascii_Art import logo
print(logo)
condition = True
my_dict = {}
while condition:
    name  = input("What is your name?: ")
    bid_amount = int(input("What's your Bid amount: $"))
    my_dict[name] =  bid_amount
    
    
    check = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
    if  check == "yes":
        clear()
    elif check == "no":
        condition = False
        for (key,value) in my_dict.items():
            max_value = max(my_dict.values())
        for key,value in my_dict.items():
            if value == max_value:
                print(f"The Winner is {key} with a bid of ${max_value}")
    else:
        print("You entered wrong option please try again!")

#In above code intead of using .max() method we also have another way of approaching below
'''
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
'''