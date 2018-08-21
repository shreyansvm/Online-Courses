# implementation of card game - Memory

import simplegui
import random

list1 = []
list1 = range(8)
list2 = []
list2 = range(8)
list_16 = []
exposed = range(16)
num_of_clicks = 0
state = 0
card_index_start = 0
card1_index = 99
card2_index = 99
equal = 0
unequal = 0


# helper function to initialize globals
def new_game():
    global list1, list2, list_16, exposed, num_of_clicks, state, unequal
    global card1_index, card2_index, card_index_start
    random.shuffle(list1)
    random.shuffle(list2)
    list_16 = list1 + list2
    for i in range(16):
        exposed[i] = 0
    num_of_clicks = 0
    state = 0
    card1_index = 99
    card2_index = 99
    card_index_start = 0
    unequal = 0
    label.set_text("Turns = 0")

def check_card_equality(index1, index2):
    global list_16, equal, unequal, state, exposed
    global card_index_start, card1_index, card2_index
    if (list_16[index1] == list_16[index2]):
        card1_index = 99
        card2_index = 99
        card_index_start = 0
        equal = 1
    else:
        unequal = 1
        equal = 0
        state = 1
        card_index_start = 0
    
def which_card(pos):
    global exposed, card1_index, card2_index, card_index_start
    global equal, unequal, status
    if pos[0]>=0 and pos[0] <= 50:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99
        if (state == 1 or state == 0):
            exposed[0]=1
        if(card_index_start == 0 and state == 0):
            card1_index = 0
            card_index_start = 1
            status = 1
        else:
            card2_index = 0
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
            
    elif pos[0]>50 and pos[0] <= 100:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        if (state == 1 or state == 0):
            exposed[1]=1
        if(card_index_start == 0):
            card1_index = 1
            card_index_start = 1
            status = 1
        else:
            card2_index = 1
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 100 and pos[0] <= 150:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        if (state == 1 or state == 0):
            exposed[2]=1
        if(card_index_start == 0):
            card1_index = 2
            card_index_start = 1
            status = 1
        else:
            card2_index = 2
            status = 2            
        if status == 2:
            check_card_equality(card1_index, card2_index)

    elif pos[0]> 150 and pos[0] <= 200:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        if (state == 1 or state == 0):
            exposed[3]=1
        if(card_index_start == 0):
            card1_index = 3
            card_index_start = 1
            status = 1
        else:
            card2_index = 3
            status = 2     
        
        if status == 2:
            check_card_equality(card1_index, card2_index)    
  
    elif pos[0]> 200 and pos[0] <= 250:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[4]=1
        if(card_index_start == 0):
            card1_index = 4
            card_index_start = 1
            status = 1
        else:
            card2_index = 4
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
                
    elif pos[0]> 250 and pos[0] <= 300:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[5]=1
        if(card_index_start == 0):
            card1_index = 5
            card_index_start = 1
            status = 1
        else:
            card2_index = 5
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
               
    elif pos[0]> 300 and pos[0] <= 350:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[6]=1
        if(card_index_start == 0):
            card1_index = 6
            card_index_start = 1
            status = 1
        else:
            card2_index = 6
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 350 and pos[0] <= 400:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[7]=1
        if(card_index_start == 0):
            card1_index = 7
            card_index_start = 1
            status = 1
        else:
            card2_index = 7
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 400 and pos[0] <= 450:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[8]=1
        if(card_index_start == 0):
            card1_index = 8
            card_index_start = 1
            status = 1
        else:
            card2_index = 8
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 450 and pos[0] <= 500:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[9]=1
        if(card_index_start == 0):
            card1_index = 9
            card_index_start = 1
            status = 1
        else:
            card2_index = 9
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 500 and pos[0] <= 550:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[10]=1
        if(card_index_start == 0):
            card1_index = 10
            card_index_start = 1
            status = 1
        else:
            card2_index = 10
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 550 and pos[0] <= 600:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[11]=1
        if(card_index_start == 0):
            card1_index = 11
            card_index_start = 1
            status = 1
        else:
            card2_index = 11
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 600 and pos[0] <= 650:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[12]=1
        if(card_index_start == 0):
            card1_index = 12
            card_index_start = 1
            status = 1
        else:
            card2_index = 12
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 650 and pos[0] <= 700:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[13]=1
        if(card_index_start == 0):
            card1_index = 13
            card_index_start = 1
            status = 1
        else:
            card2_index = 13
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 700 and pos[0] <= 750:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[14]=1
        if(card_index_start == 0):
            card1_index = 14
            card_index_start = 1
            status = 1
        else:
            card2_index = 14
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)
        
    elif pos[0]> 750 and pos[0] <= 800:
        if (unequal == 1 and card_index_start == 0 and equal == 0):
            exposed[card1_index] = 0
            exposed[card2_index] = 0
            card1_index = 99
            card2_index = 99        
        exposed[15]=1 
        if(card_index_start == 0):
            card1_index = 15
            card_index_start = 1
            status = 1
        else:
            card2_index = 15
            status = 2
            
        if status == 2:
            check_card_equality(card1_index, card2_index)        
    
# define event handlers
def mouseclick(pos):
    global exposed, num_of_clicks
    num_of_clicks += 1
    turns = str(num_of_clicks)
    label.set_text("Turns = " + turns)
    which_card(pos)
        
           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list1, list2, list_16, exposed, unequal, card1_index, card2_index
    for i in range(16):
        canvas.draw_line((50*(i), 0), (50*(i), 100), 3, 'Red')    
    for i in range(16):
        if exposed[i] == 1:
            if i >= 0 and i< 8:
                i_str = str(list_16[i])
                canvas.draw_text(i_str, ((50/4)+(50*i)-5, 75), 70, 'Red')
            elif i >= 8 and i <= 15:
                i_str = str(list_16[i])
                canvas.draw_text(i_str, ((50/4)+(50*(i))-5, 75), 70, 'Red')                                
    canvas.draw_line((0, 100), (800, 100), 3, 'Red')
    canvas.draw_text("Welcome to 'MEMORY' game", [275, 135], 22, "White")
    canvas.draw_text("TO PLAY, MATCH THE PAIR OF NUMBERED TILES IN THE ABOVE BOXES", [30, 175], 22, "White")
                
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 200)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
