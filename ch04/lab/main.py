import pygame

import random

import math

screen = pygame.display.set_mode()

width,height = pygame.display.get_window_size()


hit_box_width = width / 2
hit_box_height = height / 2

hitboxes = {
    
    "blue": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "purple": pygame.Rect(0, 0, hit_box_width, hit_box_height),
}

hitboxes["blue"].topleft = hitboxes["purple"].topright
#hitboxes["green"].topright = hitboxes["red"].bottomright
#hitboxes["purple"].topleft = hitboxes["red"].bottomright



# Define main colors
main_colors = {
 "red": (200, 0, 0),
 "green": (0, 200, 0),
 "blue": (0, 0, 200),
 "purple": (200, 0, 200),
}
# Define highlight colors
highlight_colors = {
 #"red": (255, 0, 0),
 #"green": (0, 255, 0),
 "blue": (0, 0, 255),
 "purple": (255, 0, 255),
}



#font = pygame.font.Font(None, 48)
done = False # a flag variable to determine when the program is done
result = [] # a list for the user's sequence guesses
turns = 0 # keep track of the number of turns
order = list(hitboxes.keys()) # create a shuffle-able list of colors
# pygame.draw.rect(screen, highlight_colors[color], hitboxes[color])
# pygame.display.flip()
# pygame.time.delay(1000)
for color in order:
    for c, hb in hitboxes.items(): #reset boxes to main color
        pygame.draw.rect(screen, main_colors[c], hb)
        pygame.draw.rect(screen, highlight_colors[color], hitboxes[color])
        pygame.display.flip()
        pygame.time.delay(1000)
while not done:
    for event in pygame.event.get():
    #  if event.type == pygame.KEYDOWN:
    #      if event.key == pygame.K_SPACE:
    #          random.shuffle(order)
    #          turns = len(order)
    #          result = []
    #          for color in order:
    #              for c, hb in hitboxes.items(): #reset boxes to main color
    #                  pygame.draw.rect(screen, main_colors[c], hb)
    #              pygame.draw.rect(screen, highlight_colors[color], hitboxes[color])
    #              pygame.display.flip()
    #              pygame.time.delay(1000)
    #      elif event.key == pygame.K_q:
    #          done = True
     if event.type == pygame.MOUSEBUTTONDOWN:
         turns = turns - 1
         
         if hitboxes["purple"].collidepoint(event.pos):
             result.append("purple")
             print("You have chosen user 1")
             done = True
         
         elif hitboxes["blue"].collidepoint(event.pos):
             result.append("blue")
             print("You have chosen user 2")
             done = True

         


pygame.display.flip()

screen.fill("black")
for c, hb in hitboxes.items():
    pygame.draw.rect(screen, main_colors[c], hb)

if result:
    pygame.draw.rect(screen, highlight_colors[result[-1]], hitboxes[result[-1]])

ypos = 60
# for m in msg:
#     text = font.render(m, True, "white")
#     screen.blit(text, (20, ypos))
#     ypos += 60

pygame.display.flip()



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

results = [[], []]
flag=0
for x in range(20):
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
    results[flag].append(is_in_circle)
    flag = (flag + 1) % 2




# for i in results[0]:
#     if i == True:
#         print("Number of points")
True==1
user1=results[0].count(True)
user2=results[1].count(True)



print(f"User1 made {results[0]} and User2 made {results[1]}")
if results[0]>results[1]:
    print(f"User1 won with {user1} score")
elif results[0]<results[1]:
    print(f"User2 won with {user2} score")
else:
    print("It is tie")

if result[0]=='purple' and results[0]>results[1]:
    print("You were correct about the winner")

elif result[0]=='purple' and results[0]<results[1]:
    print("You were wrong about the winner")

elif result[0]=='blue' and results[0]<results[1]:
    print("You were correct about the winner")

else:
    print("You were wrong about the winner")

