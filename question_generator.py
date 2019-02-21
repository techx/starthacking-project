import json
import random
import http.client
from html import unescape


API_ENDPOINT = "https://opentdb.com/api.php"
# Check out https://opentdb.com/api_config.php for description of how to use the OpenTDB API
# To learn more about APIs and how they work, check out https://www.dataquest.io/blog/python-api-tutorial/

def clean_question(question):
    """
    Given question dictionary, removes keys that aren't needed

    Parameters:
        question | question dictionary from api

    Returns:
        None; cleans original copy of question dictionary
    """

    # Unescape correct answer
    question["correct_answer"] = unescape(question["correct_answer"])

    # Remove keys that we don't need
    del question["incorrect_answers"]
    del question["category"]
    del question["type"]
    del question["difficulty"]


def construct_api_url(amount, difficulty, category):
    """
    Given paramters for API, constructs URL that we want to request data from

    Parameters:
        amount     | number of questions we want to retrieve
        difficulty | difficulty of questions we want
        category   | number of the category we want to use

    Returns:
        url | url for our API call with all the desired parameter
    """
    # Arguments we want in our API call
    args = {
        "amount": amount,
        "difficulty": difficulty,
        "type": "multiple",
        "category": category
    }

    url = API_ENDPOINT + "?"

    # Constructing the string with all the desired arguments
    for key, val in args.items():
        url += "&" + key + "=" + val

    return url


def get_questions():
    """
    Calls API to get a list of questions and modifies it to add "answers" key

    Returns:
        trivia_questions | List containing questions dictonaries

        question dictionary has the following keys:
            question["question"]       = question
            question["answers"]        = list of answers
            question["correct_answer"] = correct answer
    """
    url = construct_api_url("10", "easy", "18")

    # Performs API call to get questions from OpenTDB
    conn = http.client.HTTPSConnection("opentdb.com", 443)
    conn.request("GET", url)

    res = conn.getresponse().read()
    trivia_questions = json.loads(res)["results"]

    # Iterate through each question and creates the answers key in the dictionary
    for question in trivia_questions:
        # Combine incorrect and correct answers into a single list
        answers = question["incorrect_answers"]
        answers.append(question["correct_answer"])

        # Uses the random library to randomly shuffle the answers so they are in random order
        random.shuffle(answers)
        question["answers"] = answers

        # Reformats all the questions and answers from the API call to ensure it is readable
        question["question"] = unescape(question["question"])
        for idx in range(len(answers)):
            answers[idx] = unescape(answers[idx])

        # Remove all unnecessary keys from dictionary
        question = clean_question(question)

    return trivia_questions
