# Implementation of "Stopwatch: The Game"
# Istvan Kis - Interactive programming in Python - homework @ Rice University
# http://istvankis.net
# http://www.codeskulptor.org/#user40_8cxVqmzLm344LuP.py

import simplegui

# define global variables
global time, success_stops, all_stops
time = 0
all_stops = 0
success_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t/10/60
    seconds = (t - 600*minutes)/10
    tenth = t - 600*minutes - 10*seconds
    return str(minutes) + ":" + filler(seconds) + "." + str(tenth)

def filler(t):
    if len(str(t)) < 2:
        t = "0" + str(t)[0]
    return str(t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global all_stops, success_stops
    if (timer.is_running()):
        timer.stop()
        all_stops += 1
        if (time % 10 == 0):
            success_stops += 1
        timer.stop()
      
def reset():
    global time, success_stops, all_stops
    timer.stop()
    time = 0
    success_stops = 0
    all_stops = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time = time + 1
    if (time > 6000):
        timer.stop()
        time = 0
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), (100,112), 36, "Red")
    canvas.draw_text(str(success_stops) + "/" + str(all_stops), (250,30), 24, "Green")
    
# create frame
frame = simplegui.create_frame("Timer", 300, 200)

# register event handlers
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
