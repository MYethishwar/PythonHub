# Tip Calculator

## Overview

This Python script calculates the total bill with tip and evenly distributes the cost among a specified number of people. Users input the total bill amount, desired tip percentage, and the number of people splitting the bill.

## Topics Covered

1. **Input Handling**
   - *Description*: User input is gathered using the `input()` function for the total bill, tip percentage, and the number of people.
   - *Example*:
     ```python
     bill_without_tip = float(input("What was the total bill? "))
     ```

2. **Arithmetic Operations**
   - *Description*: Basic arithmetic operations are used to calculate the tip, total bill with tip, and the evenly distributed cost among the group.
   - 
     ```python
     tip = (bill_without_tip * tip_in_percentage) / 100
     ```

3. **String Formatting**
   - *Description*: String formatting, specifically f-strings, is employed to present the final output in a readable and formatted manner.
   - 
     ```python
     print(f"Each person should pay: {final_distribution_formatted}")
     ```

4. **Type Casting**
   - *Description*: Type casting is used to convert user input from strings to appropriate data types, such as converting input to float or int.
   - 
     ```python
     tip_in_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
     ```

