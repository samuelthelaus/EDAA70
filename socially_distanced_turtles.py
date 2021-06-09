import turtle
import random

turtle.Screen().delay(1)

def random_step(turtle_in):
    a = random.randint(-90, 90)
    d = random.randint(1, 10)

    turtle_in.right(a)    
    turtle_in.forward(d)
        

donatello = turtle.Turtle()
donatello.shape('turtle')
donatello.penup()
donatello.goto(-50, -50)
donatello.pendown()

michelangelo = turtle.Turtle()
michelangelo.shape('turtle')
michelangelo.penup()
michelangelo.goto(50, 50)
michelangelo.pendown()


while donatello.distance(michelangelo) > 100:
    random_step(donatello)
    random_step(michelangelo)


turtle.mainloop()
