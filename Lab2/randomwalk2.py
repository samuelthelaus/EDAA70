import turtle
import random

def random_walk(turtle_in, step_count, step_length, degrees):
    for i in range(step_count):
        turn_right = random.randint(0, 1)

        if turn_right == 1:
            turtle_in.pencolor('green')
            turtle_in.right(degrees)
        else:
            turtle_in.pencolor('red')
            turtle_in.left(degrees)
        
        turtle_in.forward(step_length)


ninja = turtle.Turtle()

random_walk(ninja, 30, 20, 45)

turtle.mainloop()