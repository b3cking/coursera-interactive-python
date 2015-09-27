# Implementation of classic arcade game Pong [easy collision]
# Istvan Kis - Interactive programming in Python - homework @ Rice University
# http://istvankis.net

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(120, 240)/60.0, -random.randrange(60, 180)/60.0]
    if(not direction):
        ball_vel[0] *= -1

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = score2 = 0
    paddle1_pos = paddle2_pos = HEIGHT / 2
    paddle1_vel = paddle2_vel = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    spawn_ball(random.randrange(0,2))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line, gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    #top-down walls collision detection
    if((ball_pos[1] - BALL_RADIUS < 0) or (ball_pos[1] + BALL_RADIUS > HEIGHT)):
        ball_vel[1] *= -1
      
    # determine whether paddle and ball collide and v:=1.1*v [Pitagoras]
    if(ball_pos[0] - BALL_RADIUS < 0 + PAD_WIDTH):
        if ((paddle1_pos - HALF_PAD_HEIGHT < ball_pos[1]) and (paddle1_pos + HALF_PAD_HEIGHT > ball_pos[1])):
            ball_vel[0] *= -1.0488
            ball_vel[1] *= 1.0488
        else:
            score2 += 1
            spawn_ball(RIGHT)
    if(ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH):
        if ((paddle2_pos - HALF_PAD_HEIGHT < ball_pos[1]) and (paddle2_pos + HALF_PAD_HEIGHT > ball_pos[1])):
            ball_vel[0] *= -1.0488
            ball_vel[1] *= 1.0488
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddles' vertical position, keep paddle on the screen
    if ((paddle1_pos + paddle1_vel - HALF_PAD_HEIGHT >= 0) and (paddle1_pos + paddle1_vel + HALF_PAD_HEIGHT <= HEIGHT)):
        paddle1_pos += paddle1_vel
        
    if ((paddle2_pos + paddle2_vel - HALF_PAD_HEIGHT >= 0) and (paddle2_pos + paddle2_vel + HALF_PAD_HEIGHT <= HEIGHT)): 
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos-HALF_PAD_HEIGHT], [PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT], [0, paddle1_pos+HALF_PAD_HEIGHT]], 1, 'Yellow', 'Yellow')
    canvas.draw_polygon([[WIDTH-PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT], [WIDTH,paddle2_pos-HALF_PAD_HEIGHT], [WIDTH, paddle2_pos+HALF_PAD_HEIGHT], [WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT]], 1, 'Yellow', 'Yellow')
       
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/2-WIDTH/10-30, 80), 60, 'White')
    canvas.draw_text(str(score2), (WIDTH/2+WIDTH/10, 80), 60, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel    
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 4    
   
def keyup(key):
    global paddle1_vel, paddle2_vel    
    if key==simplegui.KEY_MAP["up"] or key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key==simplegui.KEY_MAP["w"] or key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game)

# start frame
new_game()
frame.start()
