# IQ Test Program

def iq_test():
    print("Welcome to the IQ Test! Please answer the following 20 logical questions.")
    questions = [
        {"question": "1. What is the next number in the series: 2, 4, 8, 16, ?", "options": "A) 20 B) 22 C) 32 D) 40", "answer": "C"},
        {"question": "2. What is the day after tomorrow if today is Wednesday?", "options": "A) Friday B) Thursday C) Monday D) Saturday", "answer": "A"},
        {"question": "3. Find the odd one out: 3, 5, 7, 12, 13", "options": "A) 3 B) 7 C) 12 D) 13", "answer": "C"},
        {"question": "4. If you rearrange the letters 'CIFAIPC' you get?", "options": "A) Pacific B) Specific C) Fiction D) Ocean", "answer": "A"},
        {"question": "5. A clock shows 5:30, what is the angle between the hour and minute hand?", "options": "A) 75° B) 90° C) 45° D) 15°", "answer": "A"},
        {"question": "6. What is the smallest prime number?", "options": "A) 1 B) 2 C) 3 D) 4", "answer": "B"},
        {"question": "7. If all cats are animals and some animals are dogs, are all dogs cats?", "options": "A) Yes B) No", "answer": "B"},
        {"question": "8. What is the next letter in the sequence: A, D, G, J, ?", "options": "A) K B) M C) L D) N", "answer": "C"},
        {"question": "9. If 5 people can build 5 cars in 5 days, how many days will it take 10 people to build 10 cars?", "options": "A) 2 B) 5 C) 7 D) 10", "answer": "B"},
        {"question": "10. If you multiply all the numbers from 1 to 10, what will be the result?", "options": "A) 3,628,800 B) 45,000 C) 1,000,000 D) 9,000", "answer": "A"},
        {"question": "11. What comes next in the sequence: 1, 4, 9, 16, ?", "options": "A) 20 B) 25 C) 30 D) 36", "answer": "B"},
        {"question": "12. If a train leaves the station at 3:00 pm and travels at 80 km/h, how far will it travel by 6:00 pm?", "options": "A) 160 km B) 240 km C) 320 km D) 200 km", "answer": "B"},
        {"question": "13. Find the missing number: 9, 12, 15, 18, ?", "options": "A) 19 B) 21 C) 20 D) 24", "answer": "D"},
        {"question": "14. How many sides does a nonagon have?", "options": "A) 7 B) 9 C) 8 D) 10", "answer": "B"},
        {"question": "15. What is the synonym of 'obdurate'?", "options": "A) Flexible B) Compassionate C) Stubborn D) Generous", "answer": "C"},
        {"question": "16. Solve the riddle: I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?", "options": "A) Echo B) Cloud C) Shadow D) Flame", "answer": "A"},
        {"question": "17. What comes next in the sequence: Monday, Thursday, Sunday, Wednesday, ?", "options": "A) Saturday B) Monday C) Tuesday D) Friday", "answer": "D"},
        {"question": "18. If it takes 3 workers 3 hours to paint 3 walls, how long will it take 5 workers to paint 5 walls?", "options": "A) 3 hours B) 5 hours C) 6 hours D) 1 hour", "answer": "A"},
        {"question": "19. Which number does not belong in the series: 5, 10, 15, 25, 30", "options": "A) 15 B) 25 C) 30 D) 5", "answer": "B"},
        {"question": "20. What is 150% of 50?", "options": "A) 50 B) 75 C) 100 D) 120", "answer": "B"}
    ]

    score = 0
    total_questions = len(questions)

    for q in questions:
        print(f"\n{q['question']}")
        print(q['options'])
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            score += 1

    print(f"\nYour total score is: {score}/{total_questions}")

    if score == total_questions:
        print("Excellent! You got all answers right!")
    elif score >= total_questions * 0.7:
        print("Great job! You have a good understanding of logic.")
    elif score >= total_questions * 0.4:
        print("Not bad! But there's room for improvement.")
    else:
        print("You might want to practice more logical reasoning.")

# Start the IQ test
iq_test()
