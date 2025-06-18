from turtle import *

def drew_square(x,y):
    penup()
    goto( x , y)
    pendown()
    for _ in range(4):
        forward(100)
        right(90)
drew_square(0,0)