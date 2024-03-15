# Love Calculator

## Overview

This Python code calculates a "love score" based on the names provided by the user, combining them, converting to lowercase, and counting specific letters to determine the score. It then prints a message based on the score.

## Topics Covered

1. **Count Function**
   - *Description*: The code uses the `count()` function to count occurrences of specific letters in the combined names.

2. **Conditional Statements (if, elif, else)**
   - *Description*: The code evaluates the love score and prints a corresponding message based on different conditions.

## Example from the Code

```python
# Count Function
tcount = checking_word.count("t")

# Conditional Statements (if, elif, else)
if int_total < 10 or int_total > 90:
    print(f"Your score is {int_total}, you go together like coke and mentos.")
elif int_total > 40 and int_total < 50:
    print(f"Your score is {int_total}, you are alright together.")
else:
    print(f"Your score is {int_total}.")
