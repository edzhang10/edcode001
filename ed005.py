# SpiralFamily.py - prints a colorful spiral of names
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "purple", "blue", "green", "orange", "yellow", "white", "brown", "gray", "pink"]
family = []
# Ask for the first name
name = turtle.textinput("My family", "Enter a name or just hit [ENTER] to end:")

# Keep asking for names
while name != "":
    family.append(name)
    name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")

# Draw a spiral of the names on the screen
for x in range(100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") )
    t.left(360/len(family) + 2)


    
