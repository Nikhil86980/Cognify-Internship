"""
Level 2 - Task 1: Guessing Game
Generates a random number between 1 and 100.
The user guesses, and gets "too high"/"too low" hints until correct.
"""

import random

def play_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100. Try to guess it!")

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
    play_guessing_game()
