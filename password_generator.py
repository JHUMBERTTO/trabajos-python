import random
letters_upper_case=['A','B','C','D','E','F','G','H','I','J','K',
'L','M','N','O','P','Q','R','S','T','U','V','W','X',
'Y','Z']
letters_lower_case=['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x',
'y','z']          
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters_upper_case=int(input("How many upper case letters would you like in your password? \n"))
nr_letters_lower_case=int(input("How many lower case letters would you like in your password? \n"))
nr_symbols=int(input(f"How many symbols would you like?\n"))
nr_numbers=int(input(f"How many numbers would you like?\n"))

Password_list = []

for char in range(1, nr_letters_upper_case +1 ):
    Password_list += random.choice(letters_upper_case)

for char in range(1, nr_letters_lower_case +1):
    Password_list += random.choice(letters_lower_case)

for char in range(1, nr_symbols +1):
    Password_list += random.choice(symbols)

for char in range(1, nr_numbers +1):
    Password_list += random.choice(numbers)
   
   
Password = random.shuffle(Password_list)


password = ""

for char in Password_list:
    password += char

print(f"Your password is: {password}")

