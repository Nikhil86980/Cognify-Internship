"""
Level 2 - Task 2: Number Guesser
Same as the guessing game, but the user specifies the range themselves.
"""

import random

def play_number_guesser():
    print("Number Guesser")
    low = int(input("Enter the lowest number in the range: "))
    high = int(input("Enter the highest number in the range: "))

    secret_number = random.randint(low, high)
    attempts = 0

    print(f"I'm thinking of a number between {low} and {high}. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    play_number_guesser()
