import pygame

pygame.init()

screen= pygame.display.set_mode()

dimensions=screen.get_size()

starting_point=[dimensions[0]//2, dimensions[1]//1.5]

radius=200
for _ in range(3):
    pygame.draw.circle(screen,"white",starting_point,radius)
    starting_point[1]=starting_point[1]-radius
    radius=radius//2
    starting_point[1]=starting_point[1]-radius

    


pygame.display.flip()
pygame.time.wait(2000)