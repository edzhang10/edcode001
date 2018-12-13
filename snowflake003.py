from turtle import *

def makeFlake(length, depth, isRoot=True):

    if depth > 0:
        for branch in range(6):
            if isRoot or branch != 3:
                forward(length)
                makeFlake(length / 3, depth - 1, False)
                backward(length)

            left(60)

# tracer(False)  # because I have no patience
speed(0)

makeFlake(100, 4)
tracer(True)

hideturtle()

exitonclick()
