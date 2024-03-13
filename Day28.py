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


# Define the questions and answers in a list
questions = [
    ("What is the capital of France?", ["1. Paris", "2. London", "3. Berlin", "4. Rome"], 1, 1000),
    ("Who wrote 'Romeo and Juliet'?",
     ["1. William Shakespeare", "2. Jane Austen", "3. Charles Dickens", "4. Mark Twain"], 1, 2000),
    ("What is the chemical symbol for water?", ["1. Wo", "2. Wa", "3. H2O", "4. We"], 3, 5000),
    ("Who painted the Mona Lisa?",
     ["1. Pablo Picasso", "2. Leonardo da Vinci", "3. Vincent van Gogh", "4. Michelangelo"], 2, 10000),
    ("What is the largest mammal in the world?", ["1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Hippopotamus"], 2,
     20000)
]

# Start the game
kbc_game(questions)
