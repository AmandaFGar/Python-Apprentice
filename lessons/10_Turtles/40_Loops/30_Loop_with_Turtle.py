"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""

import turtle
turtle.setup
turtle.setup(600,600,0,0)               

tina = turtle.Turtle()                  

tina.shape('turtle')                    
tina.speed(2)                            


for i in range(8):
    tina.forward(100)
    tina.left(360/8)
