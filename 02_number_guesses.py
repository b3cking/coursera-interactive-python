# Implementation of "Guess the number" mini-project
# Istvan Kis - Interactive programming in Python - homework @ Rice University
# http://istvankis.net
# http://www.codeskulptor.org/#user40_nnwBXTPu2N_2.py

import simplegui
import random
import math

num_range=100
secret_number=0
max_try=7
actual_try=7

# helper function to start and restart the game
def new_game():
    print ""
    global secret_number
    secret_number=random.randrange(0, num_range)
    global actual_try
    actual_try = max_try
    print "--- This is a new game, start guessing [0," + str(num_range) + "]"
    print "--- You have " + str(max_try) + " guesses"

# define event handlers for control panel
def range100():
    # switching to game type - range 0-99 
    global num_range
    num_range=100
    global max_try
    max_try = int(math.ceil(math.log(num_range, 2)))
    global actual_try
    actual_try=max_try
    new_game()

def range1000():
    # switching to game type - range 0-999
    global num_range
    num_range=1000
    global max_try
    max_try = int(math.ceil(math.log(num_range, 2)))
    global actual_try
    actual_try=max_try
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    try:
        guess = int(guess)
    except ValueError:
        print "Give a valid number"
        return 1
    print "You guessed " + str(guess)
    if guess==secret_number:
        print "It is correct. You won."
        new_game()
        return 0
    elif guess>secret_number:
        print "My number is LOWER than that."
    else:
        print "My number is HIGHER than that."
    global actual_try
    actual_try -= 1
    print "You have " + str(actual_try) + " tries left."
    if actual_try == 0:
        print "You lost."
        new_game()
        return 0
    print "--"
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
