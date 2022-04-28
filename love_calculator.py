print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
combined_string_lower = combined_string.lower()

t = combined_string_lower.count("t")
r = combined_string_lower.count("r")
u = combined_string_lower.count("u")
e = combined_string_lower.count("e")

true = t + r + u + e

l = combined_string_lower.count("l")
o = combined_string_lower.count("o")
v = combined_string_lower.count("v")
e = combined_string_lower.count("e")

love = l + o + v + e 

true_love = int(str(true) + str(love))

if (true_love <10) or (true_love >90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love >=40) and (true_love <=50):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
