
## Dice stimulator
import random

def roll_dice():
    """
    Simulates rolling a standard 6-sided dice and returns the result.
    """
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")
    
    while True:
        roll = input("Roll the dice? (y/n): ").lower()
        if roll == 'y':
            result = roll_dice()
            print(f"You rolled a : {result}!")
        elif roll == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' to roll or 'n' to exit.")

if __name__ == "__main__":
    main()
