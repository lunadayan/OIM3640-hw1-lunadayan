"""
Question 2
Using the turtle library, this program will visually represent John's walk. The origin and final locatio nwill be highlighted in red. 
The program will move the turtle in random directions for the number of intersactions. The window will close when you close it. 
"""

import turtle
import random


def drunkard_walk(n):
    turtle.pencolor("red") #highlights pen color
    turtle.dot(10) #size of the dot
    turtle.fillcolor("red") #filler color

    import random

    for i in range(n):
        x,y = 0,0 #starting position
        direction = random.randint(1,4)
        if direction == 1:
            x += 100 #move right
        elif direction == 2:
            x -= 100 #move left
        elif direction == 3:
            y += 100 #move up
        elif direction == 4:
            y -= 100 #move down
        turtle.goto(x,y)

    turtle.dot(10) #dot size
    turtle.exitonclick() #exit graphic window on click

drunkard_walk(20)

