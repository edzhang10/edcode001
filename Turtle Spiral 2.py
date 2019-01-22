import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red", "green", "blue", "purple"]

for x in range(1000):
    t.color(colors[x%4])
    t.forward(2*x)
    t.left(92)
