import pygame

import random

import math

screen = pygame.display.set_mode((690,690))
screen_size_variable=pygame.display.get_window_size()
screen.fill("blue")

radius = min(screen_size_variable[0], screen_size_variable[1])//2

center = (screen_size_variable[0] // 2, screen_size_variable[1] // 2)
starting_point=(screen_size_variable[0]/2,0)         #vertical line
ending_point=(screen_size_variable[0]/2,screen_size_variable[1])

starting_point_hor=(0,screen_size_variable[1]/2)         #horizontal line
ending_point_hor=(screen_size_variable[0],screen_size_variable[1]/2)

pygame.draw.line(screen, "black" , starting_point, ending_point)

pygame.draw.line(screen, "black" , starting_point_hor, ending_point_hor)

pygame.display.flip()

pygame.draw.circle(screen,"orange",center,radius)
pygame.display.flip()

pygame.draw.line(screen, "black" , starting_point, ending_point)

pygame.draw.line(screen, "black" , starting_point_hor, ending_point_hor)
pygame.display.flip()

pygame.time.wait(2000)


#Part B


radius=10


for x in range(10):
    x= random.randrange(0,690)
    y= random.randrange(0,690)
    center=(x,y)
    distance_from_center = math.hypot(690/2-x, 690/2-y) #the distance formula
    is_in_circle = distance_from_center <= 690/2 #screen width


    
    if is_in_circle:
        pygame.draw.circle(screen,"green",center,radius)
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        pygame.draw.circle(screen,"red",center,radius)
        pygame.display.flip()
        pygame.time.wait(1000)



    

