from question_generator import get_questions

def print_question(question):
    """
    Given a question dictionary object, prints out the question in a
        way that is asking the question prompting the user for an answer
        to a multiple choice question where the options A, B, C, and D
        correspond with indices 0, 1, 2, and 3 in the question["answers"]

    Example:
        question = {
            "question": "On which computer hardware device is the BIOS chip located?",
            "answers": ["Central Processing Unit", "Motherboard",
                        "Graphics Processing Unit", "Hard Disk Drive"],
            "correct_answer" = "Motherboard"
        }

        Print out ==>

        On which computer hardware device is the BIOS chip located?
        A)	Central Processing Unit
        B)	Motherboard
        C)	Graphics Processing Unit
        D)	Hard Disk Drive

    Parameters:
        question    |   dictionary object with the keys "question", "answers",
                    |   and "correct_answer"
                    |   "question" is a string with the question we want to ask
                    |   "answers" is a list of strings with 1 correct option and
                    |       3 incorrect options
                    |   "correct_answer" is the same string as the correct option
                    |       in question["answers"]
    """
    # TODO: Implement this function as described above
    pass


def check_answer(question, user_input):
    """
    Given a question dictionary object and a user's input for answering the question,
        checks whether or not the user input is the correct option, returning
        True if it is correct, and False otherwise

    Example:
        question = {
            "question": "On which computer hardware device is the BIOS chip located?",
            "answers": ["Central Processing Unit", "Motherboard",
                        "Graphics Processing Unit", "Hard Disk Drive"],
            "correct_answer" = "Motherboard"
        }

        user_input = "C"

        return ==> False

    Parameters:
        question    |   dictionary object with the keys "question", "answers",
                    |       and "correct_answer"
                    |   "question" is a string with the question we want to ask
                    |   "answers" is a list of strings with 1 correct option and
                    |       3 incorrect options
                    |   "correct_answer" is the same string as the correct option
                    |       in question["answers"]
                    |
        user_input  |   strings of either "A", "B", "C", or "D", representing
                    |       which option answer the user selected (correspond
                    |       to indices 0, 1, 2, and 3 of question["answers"])

    Returns:
        True or False indicating whether or not the answer that the user selected
            is the correct answer according to the question dictionary
    """
    # TODO: Implement this function as described above
    pass


def is_valid_answer(user_input):
    """
    Checks if the input answer is valid of the multiple choice question

    A valid answer is one that can be used in check_answer to see if the user
        submitted the correct answer to the multiple choice question

    Example:
        answer = "C", return  ==> True
        answer = "Hello", return ==> False

    Parameters:
        user_input  |   string of what the user typed as a response to the question

    Returns:
        True or False indicating whether or the input that the user gave was valid
            according to the description above (True if valid, False otherwise)
    """
    # TODO: Implement this function as described above
    pass


def play_question(question):
    """
    Given a question dictionary object, plays out the game for the single question
    Prints out the question and all the answers and prompts the user for an input,
        then checks if the user input is correct. If the input is correct, returns True,
        otherwise False

    Parameters:
        question    |   dictionary object with the keys "question", "answers",
                    |       and "correct_answer"
                    |   "question" is a string with the question we want to ask
                    |   "answers" is a list of strings with 1 correct option and
                    |       3 incorrect options
                    |   "correct_answer" is the same string as the correct option
                    |       in question["answers"]

    Returns:
        True or False depending on whether or not the user answered correctly
            (True if correct, False otherwise)
    """
    # TODO: Print the current question

    user_input = input()

    # Keeps prompting the user for an answer until a valid one is inputted
    while not is_valid_answer(user_input):
        print("Invalid answer! Pick a letter between (A) and (D)")
        user_input = input()

    # TODO: Check the answer and tell the user whether or not they answered
    #       correctly
    # TODO: Return True if the answer is correct, and False if it's not
    pass


if __name__ == "__main__":
    """
    Main function that is run when the file is run
    Plays out entire game of trivia
    """
    # Gets list of question dictionaries
    trivia_questions = get_questions()
    score = 0

    # TODO: Loop through each question and play the game
    # for/while ...
        correct = play_question(question)

        # Updates score if the question is answered correctly
        if correct:
            score += 1

        print("Current score: " + str(score) + "/" + str(len(trivia_questions)))

    # Final scores at the end of the game
    print("That was the final question!")
    print("Final score: ", score)
