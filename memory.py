# implementation of card game - Memory

import simplegui
import random

Turns = 0
gamelist = []
exposed = []
covers = []
# helper function to initialize globals
def new_game():
    global gamelist, exposed, state, fliped1, fliped2
    state = 0
    Turns = 0
    exposed = []
    gamelist = range(8)
    gamelist.extend(gamelist)
    random.shuffle(gamelist)  
    for n in range(16):exposed.append(0)
# define event handlers
def mouseclick(pos):
    global gamelist, exposed, state, fliped1, fliped2, Turns
    # add game state logic here   
    for x in range(16):
        if 50*x <= pos[0] <= 50*x+50:         
            if state == 0:
                state = 1
                if exposed[x] == 0:
                    exposed[x] = 1                    
                    fliped2 = x
                    fliped1 = fliped2
            elif state == 1:
                state = 2
                if exposed[x] == 0:
                    exposed[x] = 1
                    fliped1 = fliped2
                    fliped2 = x
                    
            else:         
                Turns += 1
                label1.set_text('Turns = '+str(Turns))
                state = 1
                if gamelist[fliped2] == gamelist[fliped1]:
                    exposed[fliped1] = 1
                    exposed[fliped2] = 1
                else:
                    exposed[fliped1] = 0
                    exposed[fliped2] = 0
                exposed[x] = 1
                fliped2 = x 
                    

                
                    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    x = 0
    y = 0
    for n in gamelist:
        canvas.draw_text(str(n), (15+x, 70), 48, 'White')
        x += 50
    for n in exposed:
        if n == 0: 
            canvas.draw_polygon([(0+y,0),(50+y,0),(50+y,100),(0+y,100)], 1, 'Black', 'White')	          
        y += 50    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label1 = frame.add_label("Turns = 0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric