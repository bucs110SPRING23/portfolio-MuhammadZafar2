import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.speed(1)
leonardo.speed(1)

## 5. Your PART A code goes here
random_forward=random.randrange(1,101)    #RACE 1
michelangelo.forward(random_forward)
random_forward=random.randrange(1,101)
leonardo.forward(random_forward)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


for x in range(10):
    random_forward=random.randrange(1,11)
    michelangelo.forward(random_forward)
    random_forward=random.randrange(1,11)
    leonardo.forward(random_forward)
    
window.exitonclick()



# PART B - complete part B here

import pygame

import math

pygame.init()
window = pygame.display.set_mode()

side_length= 50

xpos=100
ypos=45

num_sides=[3,4,6,20,100,360]
for i in num_sides:
    points = []
    for z in range(i):
        angle = 360/i
        radians = math.radians(angle * z)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
    print(points)
    
    window.fill('black')
    pygame.draw.polygon(window,'red',points)
    pygame.display.flip()
    pygame.time.wait(2000)









window.exitonclick()
