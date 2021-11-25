#make the robot reach target by passing random barriers
#Please use this link: http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_right()
    move()
    turn_right()
    move()
    
def up():
    turn_left()
    while wall_on_right():
        move()
    jump()

def down():
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    while front_is_clear():
        move()
    up()
    down()