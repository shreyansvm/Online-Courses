# MiniProject: "Stopwatch: The Game"

import simplegui

# -------------------------------------------- #

# define global variables
width = 300
height = 200
started = False
number_of_attempts = 0
successful_attempts = 0
check_if_stop = 0
count = 0

# 0.1 sec interval
interval = 100

# -------------------------------------------- #

# define helper function score() that displays user score on the canvas
def score():
    return str(successful_attempts) + "/" + str(number_of_attempts)

# -------------------------------------------- #

# define helper function format() that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = B = C = D = 0
    D = t % 10
    
    t1 = t / 10
    C = t1 % 10
    
    t2 = t1 / 10
    B = t2 % 6
    A = t2 / 6
    
    format_str = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return format_str

# -------------------------------------------- #
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global started, check_if_stop
    started = True
    check_if_stop =  0
    timer.start()
    return

def stop_button():
    global started, count
    global number_of_attempts, successful_attempts
    global check_if_stop
    if check_if_stop == 0:
        number_of_attempts += 1
    if (format(count)[-1] == str(0)) and (check_if_stop ==  0):
        #print "Success!"
        successful_attempts += 1
    started = False
    check_if_stop = 1    
    timer.stop()
    return

def reset_button():
    global count, started, check_if_stop
    global number_of_attempts, successful_attempts
    count = 0
    number_of_attempts = 0
    successful_attempts = 0
    check_if_stop =  0
    started = False
    return

# -------------------------------------------- #

# event handler for timer with 0.1 sec interval
def increment():
    global count
    if started == True:
        count = count + 1
    else:
        count = count
    value_str = format(count)
    return value_str
# -------------------------------------------- #

# draw handler
def draw(canvas):
    #Draws stopwatch on canvas
    canvas.draw_text(format(count), [100, 115], 30, "White")
    
    #Draws Text: "Success / Attempts" on canvas
    canvas.draw_text("success / Attempts", [180, 60], 15, "Red")
    
    #Draws player score. format: successful_attempts / number_of_attempts on canvas
    canvas.draw_text(score(), [210, 85], 24, "Red")
    
    #Draws welcome text on canvas
    canvas.draw_text("Welcome to 'STOPWATCH: The Game'", [15, 15], 15, "Red")

# -------------------------------------------- #
    
# create frame
frame = simplegui.create_frame("Stop Watch", width, height)

# -------------------------------------------- #

# register event handlers
frame.add_button("Start", start_button, 200)
frame.add_button("Stop", stop_button, 200)
frame.add_button("Reset", reset_button, 200)

frame.set_draw_handler(draw)

timer = simplegui.create_timer(interval, increment)

# -------------------------------------------- #

# start frame
frame.start()
timer.start()
