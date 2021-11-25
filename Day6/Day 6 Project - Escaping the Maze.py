#Make it reach the target without hitting the obstacles
#Please use this link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#When the environment of the robot is empty, it enters an infinite loop.
#To prevent this, we must first move the robot closer to an obstacle.

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
