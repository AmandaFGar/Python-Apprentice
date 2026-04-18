"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

import random
import turtle
turtle.setup(600,600,0,0)               # Set the size of the window

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

colors = ["red", "blue", "green", "yellow", "orange"]


window = turtle.Screen()


t = turtle.Turtle() 


t.width(2) 

t.speed(0) 


# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

def make_a_shape(t):
    t.pencolor(getRandomColor())                   
    t.left(50)                       
    t.forward(50)
    t.right(70)
    t.forward(10)

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = 10

for i in range(100):
    make_a_shape(t)
    t.right(360/num_shapes)

turtle.exitonclick()
