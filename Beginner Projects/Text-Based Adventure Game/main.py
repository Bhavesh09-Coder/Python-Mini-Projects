## Text-Based Adventure Game
class AdventureGame:
    def __init__(self):
        # Initialize the game and start it
        self.game_over = False
        self.start()

    def start(self):
        # Display the welcome message and initial choices
        print("Welcome to the Forest Adventure!")
        print("You find yourself in a dark forest. You have two paths in front of you.")
        self.first_choice()

    def first_choice(self):
        # Prompt the player to choose a path
        choice = input("Do you want to go left or right? (left/right): ").lower()
        if choice == "left":
            self.left_path()
        elif choice == "right":
            self.right_path()
        else:
            # Handle invalid input and prompt again
            print("Invalid choice. Please choose again.")
            self.first_choice()

    def left_path(self):
        # Scenario for the left path
        print("You take the left path and encounter a wild animal.")
        choice = input("Do you want to run or fight? (run/fight): ").lower()
        if choice == "run":
            # Player chooses to run and wins
            print("You run away safely and find a hidden treasure!")
            self.end_game(True)
        elif choice == "fight":
            # Player chooses to fight and loses
            print("You try to fight the animal but it overpowers you.")
            self.end_game(False)
        else:
            # Handle invalid input and prompt again
            print("Invalid choice. Please choose again.")
            self.left_path()

    def right_path(self):
        # Scenario for the right path
        print("You take the right path and find a peaceful clearing.")
        choice = input("Do you want to rest or explore? (rest/explore): ").lower()
        if choice == "rest":
            # Player chooses to rest and wins
            print("You rest and regain your strength. You then find a map leading to a treasure!")
            self.end_game(True)
        elif choice == "explore":
            # Player chooses to explore and loses
            print("You explore the clearing and fall into a hidden trap.")
            self.end_game(False)
        else:
            # Handle invalid input and prompt again
            print("Invalid choice. Please choose again.")
            self.right_path()

    def end_game(self, won):
        # Display the end game message based on whether the player won or lost
        if won:
            print("Congratulations! You have successfully completed the adventure and found the treasure!")
        else:
            print("Game Over. Better luck next time.")
        self.play_again()

    def play_again(self):
        # Prompt the player to play again or exit
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            self.start()
        elif choice == "no":
            print("Thank you for playing the Forest Adventure! Goodbye!")
            self.game_over = True
        else:
            # Handle invalid input and prompt again
            print("Invalid choice. Please choose again.")
            self.play_again()


if __name__ == "__main__":
    # Create an instance of the game and start it
    game = AdventureGame()
