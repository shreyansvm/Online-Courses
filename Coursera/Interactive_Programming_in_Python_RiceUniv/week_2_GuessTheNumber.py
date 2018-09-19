# Week 2: MiniProject: Guess The Number 

# *********** Assumptions and Terminology used **************
# Number is selected between two ranges - [0, 100) or [0, 1000)
# For [0, 100) - allowed number of guesses = 7
# For [0, 1000) - allowed number of guesses = 10

# Player 1 - Computer, randomly generates a number within a specific range
# Player 1's randomly generated number is called 'player_1_choice'

# Player 2 - User, enters his/her guess in the specified text input box during run-time
# Player 2's guess is called as 'Guess'
# ************************

import random
import simplegui

# *********** GLOBAL VARIABLES **************
print "    Welcome to GUESS THE NUMBER    "
# num_range is set to selected range (100 or 1000). It is initialized to 100 because when we Run the program, the game should be started for range [0, 100)
num_range = 100

# player_1_choice is computer generated random number i.e. Player 1's selected number. It is initialized to 0
player_1_choice = 0

# remaining_guess stores the allowed number of guess for a particular range. Since default range is 100 when the game starts, remaining_guess is also initialized to 7.
remaining_guess = 7
# *************************


# *********** HELPER FUNCTION to start and restart the game **************
def new_game(nrange):    
    global player_1_choice
    global remaining_guess 
    global num_range
    
    num_range = nrange
   
    if num_range == 100:
        # random.randrange takes value : start <= value < end
        # hence as per project requirement, chosen random.randrange(0,100) so that it takes values between 0 and 99
        player_1_choice = random.randrange(0,num_range)
        remaining_guess = 7
    
    elif num_range == 1000:
        # random.randrange takes value : start <= value < end
        # hence as per project requirement, chosen random.randrange(0,1000) so that it takes values between 0 and 999
        player_1_choice = random.randrange(0,num_range)
        remaining_guess = 10
    
    print ""
    print "New game. Range is from 0 to ", num_range
    print "Number of remaining guess is ", remaining_guess
    
    return
# *************************


# *********** define EVENT HANDLERS for control panel **************
def range100():
    global player_1_choice    
    new_game(100)      
    #pass
    return

def range1000():    
    global player_1_choice
    global remaining_guess    
    new_game(1000)   
    #pass
    return
    
def input_guess(guess):
    global num_range
    global player_1_choice
    global remaining_guess
    
    guess = int(guess)
    remaining_guess = remaining_guess - 1

    print ""
    print "Guess was ", guess
    #print remaining_guess

    # Logic to check is Player 2's input choice is Higher than Player 1's randomly generated number    
    if player_1_choice < guess:
        # Logic to check is number of guesses are less than allowable guesses for a specific range
        if remaining_guess >= 0:
            print "Number of remaining guesses is ", remaining_guess 
            
            if remaining_guess != 0:
                print "Higher"
            
            # If no chance for guessesing the number is left, print GAME OVER and restart the game for the same range
            if remaining_guess == 0:
                print "You ran out of guesses. The number was ", player_1_choice
                print "Game over"
                print ""
                new_game(num_range)            
    
    # Logic to check is Player 2's input choice is Lower than Player 1's randomly generated number        
    elif player_1_choice > guess:
        if remaining_guess >= 0:
            print "Number of remaining guesses is ", remaining_guess 
            
            if remaining_guess != 0:
                print "Lower"
            
            if remaining_guess == 0:
                print "You ran out of guesses. The number was ", player_1_choice
                print "Game over"
                print ""
                new_game(num_range)
    
    # If remaining guess are still more than zero, and Player 2 get's it right (Correct), then print CORRECT and restart the game for the same range
    else:
        if remaining_guess >= 0 and (player_1_choice == guess):
            print "Correct"
            print ""
            new_game(num_range)
            
    return
# *************************


# *********** CREATE FRAME **************
frame = simplegui.create_frame("Guess The Number!!!", 100, 200)


# ****** REGISTER EVENT HANDLERS for control elements *************

# button that changes range to range [0,100)
frame.add_button("Range is [0, 100)", range100, 200)

# button that changes range to range [0,1000)
frame.add_button("Range is [0, 1000)", range1000, 200)

# Event handler that takes input guess i.e. Player 2's guess
frame.add_input("Enter a guess", input_guess, 200)
# *************************


# *********** call new_game and start frame **************
# Starting a new game for [0,100) range as per game's requirement
new_game(100)

frame.start()

# ************ END OF GAME *************

