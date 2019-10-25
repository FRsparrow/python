from turtle import *
def koch(size,n):
    if n == 1:
        fd(size)
    else:
        for angle in [0,60,-120,60]:
            left(angle)
            koch(size/3,n-1)
setup(800,500)
penup()
goto(-300,-50)
pendown()
pensize(2)
koch(600,3)
hideturtle()
