import random

number = random.randint (1, 100)
user_guess = int(input("Enter a guess 1-100: "))
guess_counter = 0

while user_guess != number and guess_counter < 5:
    if user_guess > number:
        print("Too high")
    elif user_guess < number:
        print(" Too low")
    break

guess_counter += 1
user_guess = int(input("Enter another guess: "))

print(f"Correct! The answer was {number} and it took you {guess_counter} guesses.")