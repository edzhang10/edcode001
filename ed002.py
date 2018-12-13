import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "purple", "blue", "green"]
for x in range(200):
    t.pencolor( colors[ x % 4] )
    t.circle(2*x)
    t.left(91)
