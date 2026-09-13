questions = ("Who is the richest man on earth right now?",
             "Which country experiences the first light of the rising sun?",
             "Which country has the largest area on earth?")

options = (("A. Elon Musk", "B. Steve Jobs", "C. Mark Zuckerberg", "D. Vin Diesel"),
           ("A. India", "B. Japan", "C. Russia", "D. China"),
           ("A. China", "B. India", "C. Russia", "D. Germany"))

answers = ("A", "B", "C")

user_guess = []
score = 0

for quenum, question in enumerate(questions):
    print("--------------------------------------------")
    print(question)
    for option in options[quenum]:
        print(option)

    # Get a valid answer from the user
    valid = False
    while not valid:
        guess = input(f"Enter your answer {quenum + 1} (A,B,C,D): ").upper()
        if guess in ('A', 'B', 'C', 'D'):
            user_guess.append(guess)
            valid = True
        else:
            print("Please enter a valid answer")

    # Check it immediately, using this iteration's index
    if user_guess[quenum] == answers[quenum]:
        print('Correct')
        score += 1
    else:
        print(f'Incorrect, correct is {answers[quenum]}')

print("--------------------------------------------")
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("your guesses: ", end="")
for guess in user_guess:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)

print(f"Your score is {score}% ")