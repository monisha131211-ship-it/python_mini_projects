# Project 16: Quiz Game

questions = [
    {"question": "Which function prints output in Python?",
     "options": ["a) show()", "b) print()", "c) display()"], "answer": "b"},
    {"question": "Which symbol is used for comments?",
     "options": ["a) //", "b) /*", "c) #"], "answer": "c"},
    {"question": "What is the output of 2 ** 3 ?",
     "options": ["a) 6", "b) 8", "c) 9"], "answer": "b"},
    {"question": "Which data type is [1, 2, 3] ?",
     "options": ["a) list", "b) tuple", "c) dict"], "answer": "a"},
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user = input("Your answer (a/b/c): ").lower()
    if (user == q["answer"]):
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is", q["answer"])

print(f"\nYou scored {score} out of {len(questions)}")
