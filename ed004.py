#Rosette4.py 
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
t.width(2)
number_of_circles = int(turtle.numinput("Number of circles", "How many circles in your rosette?", 6))
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
for x in range(number_of_circles):
    t.pencolor(colors[x%6])
    t.circle(100)
    t.pencolor(colors[x%6-1])
    t.circle(50)
    t.left(360/number_of_circles)
    
