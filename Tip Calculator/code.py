print("Welcome to the Tip Calculator")

#Asking user to enter total bill, tip in percentage, members.
bill_without_tip = float(input("What was the total bill? "))  # 150
tip_in_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))  # 12
members = int(input("How many people to split the bill? "))  # 5

#Calculates the Tip
tip = (bill_without_tip * tip_in_percentage) / 100
bill_with_tip = bill_without_tip + tip
group_split = bill_with_tip / members

# This makes the resultant number to format upto 2 decimal points
final_distribution_formatted = "{:.2f}".format(group_split)
print(f"Each person should pay: {final_distribution_formatted}")
