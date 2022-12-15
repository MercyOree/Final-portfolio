# Mercy O. koku
# Nov/15/2022
# Problem 5 is about how to write a function that modify the code to produce the given image.

# This code will write a function that using a code to create the correct given image.

import turtle

def drawsquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
sz = 50
for i in range(6):
    drawsquare(alex,sz)
    sz += 20
    alex.penup()
    alex.right(135)
    alex.forward(15)
    alex.left(135)
    alex.pendown()

wn.exitonclick()


