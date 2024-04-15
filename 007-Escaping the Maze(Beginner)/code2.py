''' 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def u_turn():
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and wall_in_front():
        u_turn()
    else:
        turn_right()
        move() save this code
'''
#Yethishwar code