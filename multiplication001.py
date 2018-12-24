import random
import math
import turtle
import string
import time

gamenumber = turtle.numinput("Questions", "How many questions do you want?\n", 10, 1, 30)
wn = turtle.Screen()
turtle.bgcolor("black")

def main(gamenumber):
    random.seed()
    count = 0
    correct = 0
    turtle.setpos(-100,300)
    while count < gamenumber:
        num_1 = random.randint(1,12)
        num_2 = random.randint(1,12)
        turtle.penup()
        turtle.setpos(-100,300-count*36)
        turtle.color("blue")
        turtle.write(str(num_1) + "x" + str(num_2) + "=", move=True, font=("Arial", 24, "normal"))
        guess = int(wn.numinput("Answer is", str(num_1) + "x" + str(num_2)))
        answer = num_1*num_2
        if guess == answer:
            correct += 1
            turtle.write(str(guess), move=False, font=("Arial", 24, "normal"))
        else:
            turtle.color("red")
            turtle.write(str(guess), move=False, font=("Arial", 24, "normal"))
        count += 1    

    if gamenumber > 1:
        result = correct * 100./gamenumber
    turtle.setpos(-400, 260-count*36)
    turtle.color("purple")
    turtle.write("You got " + str(result) + " percent" + " Good Job! Amy or ED!", move=False, font=("Arial", 24, "normal"))
        
main(gamenumber)
