import turtle
import pygame
import random




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
        t.right(angle)
        t.forward(distance)
        
    else:
        t.left(angle)
        t.forward(distance)
        


