# star_wars_quiz.py

questions = [
    {
        "question": "1) What is the name of Han Solo's ship?",
        "options": ["A) X-wing", "B) Millennium Falcon", "C) Star Destroyer", "D) TIE Fighter"],
        "answer": "B"
    },
    {
        "question": "2) Who is Luke Skywalker's father?",
        "options": ["A) Obi-Wan Kenobi", "B) Yoda", "C) Darth Vader", "D) Mace Windu"],
        "answer": "C"
    },
    {
        "question": "3) What color is Luke's first lightsaber?",
        "options": ["A) Blue", "B) Green", "C) Red", "D) Purple"],
        "answer": "A"
    },
    {
        "question": "4) Who says the line 'It's a trap!' in Episode VI?",
        "options": ["A) Admiral Ackbar", "B) Lando Calrissian", "C) Leia Organa", "D) C-3PO"],
        "answer": "A"
    },
    {
        "question": "5) What is the primary weapon of the Death Star?",
        "options": ["A) Ion cannon", "B) Superlaser", "C) Turbolasers", "D) Proton torpedoes"],
        "answer": "B"
    },
    {
        "question": "6) Which planet is destroyed by the Death Star in Episode IV?",
        "options": ["A) Tatooine", "B) Hoth", "C) Alderaan", "D) Naboo"],
        "answer": "C"
    },
    {
        "question": "7) Who is the Supreme Leader of the First Order in the sequel trilogy?",
        "options": ["A) Kylo Ren", "B) Snoke", "C) Palpatine", "D) Hux"],
        "answer": "B"
    }
]

def run_quiz():
    print("Welcome to the Star Wars Pop Quiz!")
    print("Type A, B, C, or D to answer.\n")

    score = 0

    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = input("Your answer: ").strip().upper()

        # basic validation
        while user_answer not in ["A", "B", "C", "D"]:
            print("Please enter A, B, C, or D only.")
            user_answer = input("Your answer: ").strip().upper()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Quiz finished! You scored {score} out of {len(questions)}.")
    if score == len(questions):
        print("Impressive, you are a true Jedi!")
    elif score >= 4:
        print("Not bad, young Padawan.")
    else:
        print("You must unlearn what you have learned and try again!")

if __name__ == "__main__":
    run_quiz()
