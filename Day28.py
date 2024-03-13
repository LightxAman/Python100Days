# Exercise
# Create a program capable of displaying questions to the users like KBC.
# Use LIST data type to store the questions and their answers.
# Display  the final amount the person is taking home after playing the game.


def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
