# Implementation of classic arcade game Pong

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

#Other Global Variables
paddle1_edge = False
paddle2_edge = False

score1 = 0
score2 = 0

ball_pos = [0, 0]
ball_vel = [0, 0]

paddle1_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]
paddle2_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]

paddle1_vel = [0, 0]
paddle2_vel = [0, 0]

# Updates score and returns score to draw_text handler
def get_score1():
    global score1
    return str(score1)
def get_score2():
    global score2
    return str(score2)

# initialize ball_pos and ball_vel for new bal in middle of table
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    hor_vel = random.randrange(2, 4)
    ver_vel = random.randrange(4, 6)
    hor_vel = 2
    ver_vel = 4
    ball_vel = [hor_vel, ver_vel] 
    
    if direction == "RIGHT":                  #True: ball moves Right
        ball_vel[1] = - ball_vel[1]
        #print "RIGHT"
    elif direction == "LEFT":                 #False: ball moves Left 
        ball_vel[0] = - ball_vel[0]
        #print "LEFT"        
        
# Event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel 
    global score1, score2  
    spawn_ball("RIGHT")
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_edge, paddle2_edge
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # When ball collides with top and bottom edges
    if ball_pos[1] >= HEIGHT- BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    #Ball and Paddle Collision code
    # For Paddle 2
    if ( (ball_pos[0] + BALL_RADIUS == WIDTH - PAD_WIDTH) and (paddle2_pos[0] <= ball_pos[1] <= paddle2_pos[1])):
        ball_vel[0] = - ball_vel[0]
    elif ( (ball_pos[0] + BALL_RADIUS == WIDTH - PAD_WIDTH) and not(paddle2_pos[0] <= ball_pos[1] <= paddle2_pos[1])):
        score1 = score1 + 1
        spawn_ball("LEFT")
        
    # For Paddle 1
    if ( (ball_pos[0] - BALL_RADIUS == PAD_WIDTH) and (paddle1_pos[0] <= ball_pos[1] <= paddle1_pos[1])):
        ball_vel[0] = - ball_vel[0]
    elif ( (ball_pos[0] - BALL_RADIUS == PAD_WIDTH) and not(paddle1_pos[0] <= ball_pos[1] <= paddle1_pos[1])):
        score2 = score2 + 1
        spawn_ball("RIGHT")
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    # For Paddle 2
    if paddle2_edge == False:
        paddle2_pos[0] +=  paddle2_vel[0]
        paddle2_pos[1] +=  paddle2_vel[1]
    if (paddle2_pos[0] <= 0 or (paddle2_pos[1] >= HEIGHT)):
        paddle2_edge = True
    
    # For Paddle 1
    if paddle1_edge == False:
        paddle1_pos[0] +=  paddle1_vel[0]
        paddle1_pos[1] +=  paddle1_vel[1]
    if (paddle1_pos[0] <= 0) or (paddle1_pos[1] >= HEIGHT):
        paddle1_edge = True
        
    # draw paddles
    canvas.draw_polygon([(WIDTH - PAD_WIDTH/2, paddle2_pos[0]), (WIDTH - PAD_WIDTH/2, paddle2_pos[1])], PAD_WIDTH+1, 'Blue')
    canvas.draw_polygon([(PAD_WIDTH/2, paddle1_pos[0]), (PAD_WIDTH/2, paddle1_pos[1])], PAD_WIDTH+1, 'Blue')

    # draw scores
    canvas.draw_text(get_score1(), (200, 100), 50, 'Red')
    canvas.draw_text(get_score2(), (400, 100), 50, 'Red')
        
def keydown(key):
    vel = 7
    global paddle1_vel, paddle2_vel, paddle1_edge, paddle2_edge
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= vel
        paddle2_vel[1] -= vel
        paddle2_edge = False

        
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[0] += vel
        paddle2_vel[1] += vel
        paddle2_edge = False        

        
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[0] -= vel
        paddle1_vel[1] -= vel
        paddle1_edge = False
        
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[0] += vel
        paddle1_vel[1] += vel
        paddle1_edge = False
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    vel = 7
    global paddle1_vel, paddle2_vel
    #tries to negate the effect of continous motion. 
    #Hence, when a certain key is pressed, velocity is negated to control motion
    
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[0] += vel
        paddle2_vel[1] += vel
        #paddle2_pos[0] +=  paddle2_vel[0]
        #paddle2_pos[1] +=  paddle2_vel[1]
        
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[0] -= vel
        paddle2_vel[1] -= vel
        #paddle2_pos[0] +=  paddle2_vel[0]
        #paddle2_pos[1] +=  paddle2_vel[1]
        
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[0] += vel
        paddle1_vel[1] += vel
        
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[0] -= vel
        paddle1_vel[1] -= vel

        
def Reset_button_handler():
    global score1, score2, paddle1_edge, paddle2_edge, ball_pos, ball_vel
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    paddle1_edge = False
    paddle2_edge = False
    score1 = 0
    score2 = 0
    ball_pos = [0, 0]
    ball_vel = [0, 0]
    paddle1_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]
    paddle2_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    spawn_ball("RIGHT")
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', Reset_button_handler)

# start frame
new_game()
frame.start()

