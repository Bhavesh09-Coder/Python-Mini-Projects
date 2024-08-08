import random

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    words = ['python', 'hangman', 'programming', 'challenge', 'developer']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6  # Number of allowed incorrect guesses
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"'{guess}' is not in the word. You have {attempts} attempts left.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word '{word}' correctly.")
            break
    else:
        print(f"\nGame over! The word was '{word}'.")

hangman_game()
