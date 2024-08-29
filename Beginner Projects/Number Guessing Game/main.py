# Project Title: Number Guessing Game

import random

def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100

    # Generate a random number between lower_bound and upper_bound
    secret_number = random.randint(lower_bound, upper_bound)

    # Initialize the number of attempts
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number between {lower_bound} and {upper_bound}.")

    # Start the guessing loop
    while True:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))

            # Increment the attempt counter
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
