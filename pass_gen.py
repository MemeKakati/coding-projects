import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

# user input on password length
pass_len = int(input("How long do you want your password? "))
password = ""

all_characters = letters + numbers + symbols

#for loop to create password
for i in range(pass_len):
    random_char = random.choice(all_characters)
    password = password + random_char
print(password)
