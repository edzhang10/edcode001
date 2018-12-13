import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
colors = ["red", "purple", "blue", "green"]
for x in range(100):
    t.pencolor( colors[ x % 4] )
    t.circle(2*x)
    t.left(91)
