# StartHacking Final Project
Now that you've seen the behind the scenes of how some software works, it's your turn to try your hand at writing some code!

We started writing some of the code for a console trivia game, but it's your job to help us finish it up and implement the functions that are missing.

## Introduction
To make a trivia game, first we need a way to generate trivia questions and answers. To do this, we use the OpenTDB API to get random questions and answers to those questions. OpenTDB API works by sending a request to one of their URLs and it returns a dictionary of the question, answers, and descriptions of the question. You can see an example of one of these dictionaries [here](https://opentdb.com/api.php?amount=1). If you want to learn more about how sending the request works, you can look at the [Getting Questions](#getting-questions) section.

We already wrote the code to get questions from OpenTDB, your task is to fill in the functions to get the game running.

## Getting Started
This project has 2 main files: `game.py` and `question_generator.py`. `game.py` is the code for running the game -- this is where you will be writing your code for the game. `question_generator.py` is the code for getting questions for our game; we have already imported that in `game.py` (you can see it at the top of the file that we imported `get_question` to the file).

## Downloading the Project
To develop this project, we used GitHub. GitHub is a way for people to share code and collaborate (like Google Drive for code!). GitHub is also a good way to save your code online in case you lose it on your computer (this is called version control, which you can learn more about [here](https://git-scm.com/book/en/v1/Getting-Started-About-Version-Control)).

You can download the project to your computer by downloading a zip file or using git. If you have a GitHub account and it is configured on your computer, open your terminal and run `git clone https://github.com/techx/starthacking-project.git` or `git clone git@github.com:techx/starthacking-project.git` if you have your SSH key configured on GitHub. If you do not have git configured, you can click the green "Clone or Download" button and click "Download ZIP".

## Making the Game
We already wrote the code for getting the questions in `question_generator.py`; now it's your turn to go through `game.py` and finish the functions that say `pass` or places that say `TODO` so we can actually use the questions in a trivia game. Each function has a description on what they're supposed to do, so your task is to implement the functions so that it works as described.

We can start by looking at the bottom of the page where it says `if __name__ == "__main__:"`. This is the part of the file that will run when you run `python game.py`. To get this to work, make sure that the main section and each function are fully implemented.

Once you are satisfied, you can test your game by running `python game.py` in your terminal in the directory of the project. If you have it working and you want to try some more challenges, you can try those listed in [Optional Challenges](#optional-challenges). If you find a bug, try to go through the game again and debug the code.

You only need to change `game.py` to finish the game. If you want to try the optional challenges or see how we use the API, you can look through `question_generator.py`.

<div id="getting-questions"></div>

## Getting Questions
When we enter a URL into our browser, there are typically 2 major parts to the URL. If we look at the URL `https://opentdb.com/api.php?amount=10`, this is saying that we want to access the `https://opentdb.com/api.php` server and pass in an argument `amount=10`. These are separated by the `?` in the URL. In this case, `amount` is the number of questions we want to get. If we want 5 questions, we can go to the URL `https://opentdb.com/api.php?amount=5`. If you want to get 5 questions and set the difficulty to medium, we can pass in multiple arguments by separating them with `&` like `https://opentdb.com/api.php?amount=5&difficulty=medium`.

If you want to learn more about how APIs work, click [here](https://www.dataquest.io/blog/python-api-tutorial/). If you want to learn more about OpenTDB API, click [here](https://opentdb.com/api_config.php).

<div id="optional-challenges"></div>

## Optional Challenges
If you finish the project early and would like to try and tackle some of our challenges, try your hand at implementing these features (you may have to look into `question_generator.py` for some of these):
 - Prompt user to select difficulty at the beginning of the game
 - Prompt user to select number of questions at the beginning of the game
 - Prompt user to select category at the beginning of the game (look at [Categories for the API](#category-ids) for category IDs)
    - You should prompt the user for an input in a user-friendly manner. In other words, you should not assume that the user knows the category IDs beforehand.
 - Make the game keep asking questions until user gets one wrong (instead of having a set number of questions)

If you find yourself stuck, check out the [Hints](#hints) section below

<div id="category-ids"></div>

## Categories for the API
The `category` argument for the API uses category IDs rather than category names for selecting a category. Below is the mapping of category IDs to category names:

ID | Name
--- | ---
9 | General Knowledge
10 | Entertainment: Books
11 | Entertainment: Film
12 | Entertainment: Music
13 | Entertainment: Musicals & Theatres
14 | Entertainment: Television
15 | Entertainment: Video Games
16 | Entertainment: Board Games
17 | Science & Nature
18 | Science: Computers
19 | Science: Mathematics
20 | Mythology
21 | Sports
22 | Geography
23 | History
24 | Politics
25 | Art
26 | Celebrities
27 | Animals
28 | Vehicles
29 | Entertainment: Comics
30 | Science: Gadgets
31 | Entertainment: Japanese Anime & Manga
32 | Entertainment: Cartoon & Animations

<div id="hints"></div>

## Optional Challenge Hints
 - Try to see how we make the URL that we send to the API and think about how you can modify that for what you're trying to do
    - You may find it useful to make changes to `get_questions` so that it takes in any parameters you need for your changes
 - It may be useful to use dictionaries to store any mappings you need
 - You may need to change where we get questions and when we exit the loop of asking questions
