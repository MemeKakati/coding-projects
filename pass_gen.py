import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

# pick a random character
random_letter = random.choice(letters)
print(random_letter)

# user input on password length
pass_len = int(input("How long do you want your password? "))

for letter in letters:
    for number in numbers:
        for symbol in symbols:
            print(letter, numbers, symbols)
    break