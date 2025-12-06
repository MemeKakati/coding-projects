# importing library
import random

# random number variable
random_number = random.randint(1, 50)

# counting numner of guesses
guess_count = 0

# max number of attempts
max_attempts = 10

# user input for guess
user_input = int(input("Enter your guess: "))

# while loop to keep the game going until the user guesses correctly
while user_input != random_number:
    guess_count += 1
    if user_input != random_number and guess_count < max_attempts:
        print("Your guess is too low.")
    else:
        print("Your guess is too high")
    user_input = int(input("Enter a new guess: "))
guess_count += 1

print(f"Congratulations! You guessed the number {random_number} correctly in {guess_count} guesses! ")

    

