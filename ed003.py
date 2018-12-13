import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 6
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
for x in range(360):
    t.pencolor( colors[ x % sides] )
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(2)
    t.left(90)
