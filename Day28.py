# Exercise
# Create a program capable of displaying questions to the users like KBC.
# Use LIST data type to store the questions and their answers.
# Display  the final amount the person is taking home after playing the game.


def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")


def kbc_game(questions):
    total_questions = len(questions)
    current_question = 0
    amount = 0

    while current_question < total_questions:
        q, options, answer, prize = questions[current_question]
        display_question(q, options)
        choice = int(input("Enter your choice (1-4): "))

        if choice == answer:
            print("Correct Answer!")
            amount += prize
            print(f"You won {prize}! Total amount: {amount}")
        else:
            print("Sorry, wrong answer!")
            break

        current_question += 1

    print(f"Congratulations! You've completed the game. Total amount won: {amount}")
