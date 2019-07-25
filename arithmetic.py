# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:58:33 2019

@author: dletran
"""

#%% I. Initialize
import numpy as np
from random import randrange

menu =  ("""Welcome to the arithmetic game. 
  1) Addition
  2) Subtraction
  3) Multiplication
  4) Division
  5) Exit.""")

operator_choice = {'addition' : '+',
                   'subtraction' : '-',
                   'multiplication ': '*',
                   'division' : '÷'}

game_choice = {1 : 'addition',
               2 : 'subtraction',
               3 : 'multiplication',
               4 : 'division'}


#%% II. Functions

def take_input(question, ls_choices):
    user_input = None
    while user_input not in ls_choices:
        if user_input is not None:
            print("Please enter a valid choice.")
            print(menu)
        try:
            user_input = input(question)
            user_input = int(user_input)
        except ValueError:
            if user_input.lower() in ['yes', 'ye', 'y', 'no', 'n']:
                return user_input
            continue
    return user_input

def take_answer(x, y, operator):
    user_input = None
    operator = operator_choice[operator]
    while type(user_input) is not int:
        if user_input is not None:
            print("Please enter a valid answer.")
        try:
            user_input = int(input(f'What is {y} {operator} {x}? >> '))
        except ValueError:
            user_input = 0
            continue
    return user_input

def evaluate_answer(computer, user):
    exit_statement = "Hit ENTER to exit to the main menu"
    if user == computer:
        print(f"CORRECT!! Good work. {exit_statement}")
        bool_answer = True
    else:
        print(f"WRONG, The answer is: {computer}. {exit_statement}")
        bool_answer = False
    print("")
    return bool_answer
    
def setup():
    x = np.random.randint(low=0, high=10)
    y = np.random.randint(low=0, high=100)
    return x, y

def the_math_part(x, y, arithmetic_type):
    if arithmetic_type == 1:
        return x + y
    elif arithmetic_type == 2:
        return y - x
    elif arithmetic_type == 3:
        return x * y
    elif arithmetic_type == 4:
        return round(x / y, 2)
    elif arith

def math_game(arithmetic_type):
    x, y = setup()
    computer_answer = the_math_part(x, y, arithmetic_type)
    user_answer = take_answer(x, y, game_choice[arithmetic_type])
    bool_answer = evaluate_answer(computer_answer, user_answer)
    return user_answer, bool_answer


#%% deprecated functions
def addition():
    x, y = setup()
    computer_answer = x + y
    user_answer = take_answer(x, y, 'addition')
    bool_answer = evaluate_answer(computer_answer, user_answer)
    return user_answer

def subtraction():
    x, y = setup()
    computer_answer = y - x
    user_answer = take_answer(x, y, 'subtraction')
    bool_answer = evaluate_answer(computer_answer, user_answer)
    return user_answer

def multiplication():
    x, y = setup()
    computer_answer = x * y
    user_answer = take_answer(x, y, 'multiplication')
    evaluate_answer(computer_answer, user_answer)
    return user_answer

def division():
    x, y = setup()
    computer_answer = x / y
    print("Round to the nearest 100th if necessary.")
    user_answer = take_answer(x, y, 'division')
    evaluate_answer(computer_answer, user_answer)
    return user_answer
    
#%% III. Set-Up and run for Game

score_correct = 0
score_wrong = 0

while 1:
    print(menu)
    question = 'What would you like to do? Select one >> '
    ls_choices = [1, 2, 3, 4, 5, 'exit', 'exit()', 'exit.']
    user_input = None; user_answer = None # flush
    user_input = take_input(question, ls_choices)
    print(user_input)
    if user_input == 5:
        break
    elif str(user_input).lower() in ['exit','exit()', 'exit.']:
        break
    while user_answer != 0:
        user_answer, bool_points = math_game(user_input)
        if bool_points:
            score_correct += 1
        else:
            score_wrong += 1
        
score_total = score_correct + score_wrong
score_percent = round(score_correct / score_total, 1) * 100

print(f"""
      Grade: {score_percent} %
      Correct: {score_correct}
      Wrong: {score_wrong}
      Questions Answered: {score_total}
      """)













