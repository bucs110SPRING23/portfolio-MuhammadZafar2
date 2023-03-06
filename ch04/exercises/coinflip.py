import turtle
import pygame
import random


# def is_in_screen(w,t):
#     left_bound=w.window_width()/2
#     right_bound=w.window_width()/2
#     top_bound=w.window_height()/2
#     bottom_bound=w.window_height()/2

t=turtle.Turtle()
t.shape("turtle")
t.speed(1)
wn=turtle.Screen()
wn.bgcolor("yellow")




colors=["red","green","blue","purple","red"]
distance=50
angle=90
is_in_screen=True
while is_in_screen:
    coin=random.randrange(0,2)
    if coin%2==0:
        wn.right(angle)
        wn.forward(distance)
    else:
        wn.left(angle)
        wn.forward(distance)


    turtleX=t.xcor()
    turtleY=t.ycor()
point()


    x_range=wn.window_width()/2
    y_range=wn.window_height()/2
if 