"""
# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]


def run_quiz(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        print(question["options"])
        your_answer=input("what is your answer? (A,B,C,D): ").upper()
        if your_answer==question["answer"]:
            print("it is true")
            score+=1
        else:
            print("ASXSALXKSAKDAD, Wrong!!")
    print(f"your score :{score}")

# Run the quiz
run_quiz(questions)

"""