import maze
import turtle

# Select maze 1-5
print('Välj en labyrint från 1-5:')
maze_selection = int(input())
if maze_selection == 5:
    turtle.Screen().delay(1)

# Load maze
m = maze.Maze(maze_selection)

# Create and move turtle
stefan = turtle.Turtle()
stefan.shape('turtle')
stefan.shapesize(.25)
stefan.penup()
x, y = m.entry()
stefan.goto(x, y)
stefan.pendown()
stefan.left(90)

# Step into maze
stefan.forward(1)


while not m.at_exit(stefan.pos()):

    # Get direction and position
    direction = stefan.heading()
    pos = stefan.pos()

    # Turn to make sure nothing is in front and wall to the left
    if not m.wall_at_left(direction, pos):
        stefan.left(90)
    elif m.wall_in_front(direction, pos):
        stefan.right(90)
        direction = stefan.heading()
        pos = stefan.pos()
        if m.wall_in_front(direction, pos):
            stefan.right(90)
    
    
    # Take a step forward
    stefan.forward(1)


        

# Keep window open
turtle.Screen().mainloop()