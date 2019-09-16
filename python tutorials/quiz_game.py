# -*- coding: utf-8 -*-
# Python Quiz Game
import os
import random


# the bank of questions is stored as a Python dictionary so that answers can be 
# looked up using the questions as keys, For Example:
# answer = QUESTION_BANK[question]
QUESTION_BANK = {
    'What is the 4th planet from our sun?': 'Mars',
    'Which planet has the tallest volcano in the solar system?': 'Mars',
    'Which planet is commonly called "the Red Planet"?': 'Mars',
    'Which planet was named after the Greek god `Ares`?': 'Mars',
    'Which planet has two moons called `Phobos` and `Deimos`?': 'Mars'
}


def introduce_game():
    """
    The message that prints when the quiz game script runs
    """
    message = '\U0001F30C\nWelcome to the Girl Scout Quiz Game!\nTry to answer all of the questions!'
    print('\n')
    print('-'*40)
    print(message)


def ask_question(question, points):
    """
    prompt user for the correct answer to a question from the question bank
    """

    # instructions for how to answer the question
    print('\nType your answer and hit the "enter" key.')
    
    # ask the question
    print('QUESTION: {}'.format(question))
    print('ANSWER: ')
    
    # the user's typed input is assigned to the 'response' variable
    response = input()

    # check if the response is correct
    if response == QUESTION_BANK[question]:
        
        # print a random congrats message
        print(get_congratulations())
        
        # add 1 to the total game score
        points += 1

    # if the answer was incorrect, prompt for another answer
    else:
        # need to decide - how many tries for a question does the player get?
        print('Try Again!')
        response = input()

    # return the new total game score
    return points


def validate_answer(question, answer):
    """
    check if answer matches the correct answer from the bank, even if 
    capitalization is different.
    """
    if answer.lower() == QUESTION_BANK[question].lower():
        return True
    else:
        return False


def report_score(points, game_mode):
    """
    print out the score for the game and ask the player if they want to
    play again.
    """

    # clear the console
    os.system('clear')
    
    # fancy console output
    print('*'*40)

    # print the total game score
    print('Your score is {} points!  Do you want to play again? (y/n)\n'.format(points))
    
    # prompt user to decide if they want to play again
    play_again = input()

    # play again if the answer is 'y' or 'Y'
    if play_again.lower() == 'y':
        points = 0
        
        # run the game again (either regular or random mode)
        if game_mode == 'normal':
            run_game()

        elif game_mode == 'random':
            run_game_randomized()

    # for all other answers, exit the game and say goodbye
    else:
        print('\nThanks for playing!  Goodbye.')


def run_game():
    """
    run a standard quiz game in the order of the questions listed in
    the question bank variable
    """

    # starting points total
    points = 0

    # starting message for the game
    introduce_game()

    # loop through the question bank and ask each question
    for question in QUESTION_BANK.keys():

        # the total points changes after each question
        points = ask_question(question, points)

    # end the game by reporting the point total
    report_score(points, game_mode='normal')


def run_game_randomized():
    """
    run a standard quiz game with a randomized question order for the 
    questions listed in the question bank variable
    """

    # starting points total
    points = 0

    # starting message for the game
    introduce_game()

    # define a list of questions so that we can remove a question after
    # it has already been asked
    question_list = list(QUESTION_BANK.keys())

    # if there are still questions in the question list, ask a question
    while len(question_list) > 0:

        # get a random index based on the current length of the question list 
        question_index = random.randint(0, len(question_list) - 1)
        
        # access the question from the current list
        question = question_list[question_index]
        
        # the total points changes after each question
        points = ask_question(question, points)

        # remove that question from the question list
        question_list.pop(question_index)

    # end the game by reporting the point total
    report_score(points, game_mode='random')


def get_congratulations():
    """
    get a randomized message for when the player gets a question right
    """
    congrats_messages = [
        'Correct!',
        'Great Job!',
        'Nice Work!',
        'Tres Bien!',
        '¡Muy Bién!',
        '축하해',
        'Correct!',
        "That's Right!",
        '好极了',
        'Kazi nzuri',
    ]
    message_index = random.randint(0, len(congrats_messages) - 1)
    return congrats_messages[message_index]


if __name__ == '__main__':

    run_game()
