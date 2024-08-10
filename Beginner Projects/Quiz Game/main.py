## Quiz-Game:
import random

def load_questions():
    """
    Load the quiz questions.
    
    :return: A list of dictionaries containing questions and their options.
    """
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A. Harper Lee", "B. Jane Austen", "C. J.K. Rowling", "D. Mark Twain"],
            "answer": "A"
        }
    ]
    return questions

def ask_question(question):
    """
    Ask a single question to the user.
    
    :param question: A dictionary containing the question, options, and correct answer.
    :return: True if the user answered correctly, False otherwise.
    """
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    return user_answer == question["answer"]

def quiz():
    """
    Run the quiz game.
    """
    print("Welcome to the Quiz Game!")
    questions = load_questions()
    random.shuffle(questions)  # Shuffle questions for a different order each time

    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
        print()  # Print a blank line for better readability

    print(f"Quiz over! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    quiz()
