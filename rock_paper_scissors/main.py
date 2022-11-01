'''
Rock Paper Scissors SOLUTION 🚀🔥
Concepts covered in this project:
    👉 Variables
    👉 Conditionals (if elif)
    👉 String Interpolation
    👉 Databases
    👉 Routing
    👉 Functions
    👉 Random
'''

from flask import Flask, render_template, request
from random import choice
from database import db

app = Flask(__name__)

# Check if the following keys exist in the database; if not create them
if 'game_start' not in db:
  db['game_start'] = False

if 'player_score' not in db:
    db['player_score'] = 0

if 'choices' not in db:
    db['choices'] = ''

if 'result' not in db:
    db['result'] = ''


@app.route('/')
def index():
    # update the values to be dynamic and rely on the database
    return render_template('index.html', 
                           game_start=False,
                           player_score=0,
                           choices='',
                           result='')


# ** Calculate who won and show it on the screen **
@app.route('/play', methods=['POST'])
def play():
    # change the state of game_start in the database to True
  
    # get human choice from url arguments & save humans choice in a variable
    # request.args['choice'] 👉 will get you the player choice as a string
    
    # generate a choice on behalf of the computer then save it in a variable

    # calculate score of the player vs. computer choice

    # update result, choices and player_score in the database

    # render the index.html file with dynamic values
    return render_template('index.html',
                           game_start=False,
                           player_score=0,
                           choices='',
                           result='')


'''
** get_computer_choice randomly selects between `rock` `paper` `scissors` and returns that string **
get_computer_choice() 👉 'Rock'
get_computer_choice() 👉 'Scissor
'''
def get_computer_choice():
    pass

'''
** calculate_result compares player_move & computer_move and returns the score accordingly **
human wins - calculate_result('Rock', 'Scissors') 👉 1
human loses - calculate_result('Scissors', 'Rock') 👉 -1
human draws - calculate_result('Rock', 'Rock') 👉 0
'''
def calculate_result(player_choice, computer_choice):
    # Create a variable called `score` and set it's value to None

    # All situations where human draws, set `score` to 0

    # All situations where human wins, set `score` to 1
    # make sure to use elifs here

    # Otherwise human loses (aka set score to -1)

    # return score
    pass


'''
get_result returns a string with a value of `You Win!` or `You Lose!` or 
`It's a Draw!` based on the score.

>>> get_result(1)
"You Win!"

>>> get_result(-1)
"You Lose!"

>>> get_result(0)
"It's a Draw!"
'''
def get_result(score):
    pass

# ** end_game resets every value to its initial value **
@app.route('/end')
def end_game():
    return render_template('index.html', 
                           game_start=False,
                           player_score=0,
                           choices='',
                           result='')


# Replit server config
app.run(host='0.0.0.0', port=81)

# Local Machine
app.run(debug=True)
