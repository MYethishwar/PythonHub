name1 = input("Enter boy name: ") # What is your name?
name2 = input("Enter girl name: ") # What is their name?
#Concatenating the names.
checking_word = name1 + name2

#Converting into the lowercase letters. 
checking_word = checking_word.lower()

true_count = 0

#TRUE Checking.
tcount = checking_word.count("t")
rcount = checking_word.count("r")
ucount = checking_word.count("u")
ecount = checking_word.count("e")
total_true_count = tcount + rcount + ucount + ecount


#LOVE Checking.
lcount = checking_word.count("l")
ocount = checking_word.count("o")
vcount = checking_word.count("v")
total_love_count = lcount + ocount + vcount + ecount

#Concatenating the count of 2 words i.e TRUE, lOVE.
Total =str(total_true_count) + str(total_love_count)
int_total = int(Total)


#As per  the given conditions printing the results.
print("The Love Calculator is calculating your score...")
if int_total < 10 or int_total > 90:
  print(f"Your score is {int_total}, you go together like coke and mentos.")
elif int_total > 40 and int_total < 50:
  print(f"Your score is {int_total}, you are alright together.")
else:
  print(f"Your score is {int_total}.")