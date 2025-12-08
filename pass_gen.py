import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

# pick random characters
random_letter = random.choice(letters)
random_numbers = random.choice(numbers)
random_symbols = random.choice(symbols)

# user input on password length
pass_len = int(input("How long do you want your password? "))
password = ""
#for loop to create password
for i in range(pass_len):
    random_letter = random.choice(letters)
    password = password + random_letter
    random_numbers = random.choice(numbers)
    password = password + random_numbers
    random_symbols = random.choice(symbols)
    password = password + random_symbols
print(password)
