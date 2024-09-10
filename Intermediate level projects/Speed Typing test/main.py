## Project Title : Speed Typing test

import time
import random

# List of sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Typing tests are a great way to measure typing speed.",
    "Practice makes perfect when it comes to typing.",
    "Fast and accurate typing is an essential skill."
]

# Function to calculate typing speed
def typing_speed_test():
    # Randomly select a sentence
    sentence = random.choice(sentences)
    print("\nTyping Speed Test")
    print("Type the following sentence as quickly and accurately as possible:\n")
    print(f"Sentence: {sentence}")
    
    input("Press Enter when you are ready to start...")

    # Record the start time
    start_time = time.time()

    # User input
    user_input = input("\nStart typing here: ")

    # Record the end time
    end_time = time.time()

    # Calculate typing speed and accuracy
    time_taken = end_time - start_time
    time_taken = round(time_taken, 2)  # Round to 2 decimal places

    # Words per minute (WPM) calculation
    words_in_sentence = len(sentence.split())
    words_per_minute = (words_in_sentence / time_taken) * 60

    # Accuracy calculation
    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(sentence) and c == sentence[i])
    accuracy = (correct_chars / len(sentence)) * 100

    # Print results
    print(f"\nTime taken: {time_taken} seconds")
    print(f"Words per minute (WPM): {round(words_per_minute, 2)}")
    print(f"Accuracy: {round(accuracy, 2)}%")

# Run the typing speed test
if __name__ == "__main__":
    typing_speed_test()
