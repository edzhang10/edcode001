import turtle
import random

# setup the window with a background colour
ed = turtle.Screen()
ed.bgcolor("black")

# assign a name to your turtle
amy = turtle.Turtle()
amy.speed(0)
amy.pensize(2)

# create a list of colours
sfcolor = ["white"]

# create a function to create different size snowflakes
def snowflake(size):
# move the pen into starting position
    amy.penup()
    amy.forward(10*size)
    amy.left(45)
    amy.pendown()
    amy.color(random.choice(sfcolor))
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)   
        amy.left(45)
    

# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            amy.forward(10.0*size/3)
            amy.backward(10.0*size/3)
            amy.right(45)
        amy.left(90)
        amy.backward(10.0*size/3)
        amy.left(45)
    amy.right(90) 
    amy.forward(10.0*size)

# loop to create 20 different sized snowflakes with different starting co-ordinates
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(2, 6)
    amy.penup()
    amy.goto(x, y)
    amy.pendown()
    snowflake(sf_size)

# leave the window open until you click to close  
ed.exitonclick()  
