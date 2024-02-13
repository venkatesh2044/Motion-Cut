# Define the Quiz class
class Quiz:
    # Initialize the Quiz with an empty list of questions and a score of 0
    def __init__(self):
        self.questions = []
        self.score = 0

    # Method to add a question to the quiz
    def add_question(self, question, options, answer):
        # Each question is a dictionary with the question text, options, and the correct answer
        self.questions.append({
            'question': question,
            'options': options,
            'answer': answer
        })

    # Method to start the quiz
    def start(self):
        # Loop through each question
        for i, q in enumerate(self.questions):
            # Print the question
            print(f"Q{i+1}: {q['question']}")
            # Print the options
            for j, option in enumerate(q['options']):
                print(f"{j+1}. {option}")
            # Get the user's answer
            answer = input("Your answer: ")
            # Check if the answer is correct
            if q['options'][int(answer)-1].lower() == q['answer'].lower():
                # If correct, increment the score and print a message
                self.score += 1
                print("Correct!\n")
            else:
                # If incorrect, print the correct answer
                print(f"Incorrect! The correct answer is {q['answer']}.\n")
        # At the end of the quiz, print the final score
        print(f"Quiz completed! Your final score is {self.score} out of {len(self.questions)}.")

# Usage
quiz = Quiz()  # Create a Quiz object
# Add questions to the quiz
quiz.add_question("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris")
quiz.add_question("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "F. Scott Fitzgerald"], "Harper Lee")
quiz.add_question("What is the square root of 81?", ["9", "8", "7"], "9")
quiz.start()  # Start the quiz
