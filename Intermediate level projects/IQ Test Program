# Project Title : IQ Test Program

# Function to ask a question and get user's answer
def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    answer = input("Enter your answer (1-4): ")

    # Validate user input
    while answer not in ['1', '2', '3', '4']:
        answer = input("Invalid input. Please enter a number between 1 and 4: ")

    # Return True if the answer is correct
    return int(answer) == correct_option

# List of questions and options
questions = [
    {
        "question": "What is the next number in the sequence: 2, 4, 8, 16, ... ?",
        "options": ["20", "24", "32", "48"],
        "correct": 3
    },
    {
        "question": "Which word is the odd one out?",
        "options": ["Apple", "Banana", "Carrot", "Grapes"],
        "correct": 3
    },
    {
        "question": "If all squares are rectangles, but not all rectangles are squares, which statement is true?",
        "options": ["All rectangles are squares", 
                    "All squares are rectangles", 
                    "No squares are rectangles", 
                    "Some rectangles are squares"],
        "correct": 2
    },
    {
        "question": "Which of the following numbers is a prime number?",
        "options": ["18", "29", "42", "51"],
        "correct": 2
    },
    {
        "question": "What is the cube root of 27?",
        "options": ["2", "3", "9", "6"],
        "correct": 2
    }
]

# Main program
def iq_test():
    print("Welcome to the IQ Test!")
    score = 0

    # Loop through each question
    for i, question_data in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        if ask_question(question_data["question"], question_data["options"], question_data["correct"]):
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")
    
    # Display final score
    print(f"\nYour total score: {score} out of {len(questions)}")
    
    # Display interpretation of score
    if score == len(questions):
        print("Excellent! You have a high IQ!")
    elif score >= len(questions) // 2:
        print("Good job! You have an average IQ.")
    else:
        print("Keep practicing! You can improve.")

# Run the IQ test
if __name__ == "__main__":
    iq_test()
