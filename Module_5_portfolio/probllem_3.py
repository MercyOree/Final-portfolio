# Mercy Oreoluwa Koku
# Nov/1/2022

# This program uses the turtle method and draws a triangle or square of your choice.

import turtle
wn = turtle.Screen()
Tom = turtle.Turtle()
Length_of_a_side = int(input("Enter the side the length of your choice: "))
Fill_color = input("Enter in the fill color of your choice: ")
Shape = input("Enter what shape you want, a triangle or square: ")

if Shape == "triangle":
    Tom.fillcolor(Fill_color)
    Tom.begin_fill()
    for triangle in range(3):
        Tom.forward(Length_of_a_side)
        Tom.left(120)
    Tom.end_fill()
else:
    Tom.fillcolor(Fill_color)
    Tom.begin_fill()
    for square in range(4):
        Tom.forward(Length_of_a_side)
        Tom.left(90)
    Tom.end_fill()

wn.exitonclick()


