# Implementation of card game Memory
# Istvan Kis - Interactive programming in Python - homework @ Rice University
# http://istvankis.net

import simplegui
import random

global decks, exposed_list, state, prev_idx, prev2_idx, turn

# reset & new game
def new_game():
    global decks, exposed_list, state, prev_idx, prev2_idx, turn
    list1 = list2 = range(8)
    decks = list1 + list2
    random.shuffle(decks)
    exposed_list = []
    for i in range(16):
        exposed_list.append(False)
    state = prev_idx = prev2_idx = turn = 0

# mouse event handler with logic
def mouseclick(pos):
    global decks, exposed_list, state, prev_idx, prev2_idx, turn
    clicked_idx = pos[0] // 50
    # before start
    if state == 0:
        exposed_list[clicked_idx] = True
        prev_idx = clicked_idx
        state = 1
    # 1 card is exposed    
    elif state == 1:
        if (exposed_list[clicked_idx] == False):
            exposed_list[clicked_idx] = True                 
            turn += 1
            prev2_idx = prev_idx
            prev_idx = clicked_idx
            state = 2
    # 2 card is exposed            
    else:
        if (exposed_list[clicked_idx] == False):
            if (decks[prev_idx] == decks[prev2_idx]):
                exposed_list[prev_idx] = exposed_list[prev2_idx] = True
            else:
                exposed_list[prev_idx] = exposed_list[prev2_idx] = False        
            exposed_list[clicked_idx] = True
            prev_idx = prev2_idx = clicked_idx
            state = 1
                        
# cards are logically 50x100 pixels in size
def draw(canvas):
    n = 0
    global decks, exposed_list
    for deck, exposed in zip(decks, exposed_list):
        canvas.draw_text(str(deck), (n+15, 60), 50, 'White')
        if not exposed:
            canvas.draw_polygon([[n, 0], [n+50, 0], [n+50, 100], [n, 100]], 2, 'Green', 'Green')
            canvas.draw_line((n+50, 0), (n+50, 100), 5, 'Black')
        n = n + 50
    label.set_text("Turn: " + str(turn))
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns: 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
