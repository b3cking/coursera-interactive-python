# Implementation of Rock-paper-scissors-lizard-Spock game
# Istvan Kis - Interactive programming in Python - homework @ Rice University
# http://istvankis.net
# http://www.codeskulptor.org/#user40_FVJBczofY9_1.py

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        print "Error in format."

def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else:
        print "Error in format."

def rpsls(player_choice):     
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)	
    print "Player chooses " + player_choice
    print "Computer chooses " + comp_choice
    modulo = (comp_number-player_number)%5
    
    if modulo==1 or modulo==2:
        print "Computer wins!"
    elif modulo==3 or modulo==4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
    print ""
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
