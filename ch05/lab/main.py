import pygame





def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count

# x=threenp1(4)
# print(x)

def threenp1range(upper_limit):
    objs_in_sequence = { }
    for i in range(2,upper_limit+1):
        x=threenp1(i)
        objs_in_sequence[i]=x
    return objs_in_sequence


# def main():
#     threenp1range(10)

# if __name__ == "__main__":
# main()





def graph_coordinates(objs_in_sequence):
    screen = pygame.display.set_mode((690,690))
    new_display = pygame.transform.flip(screen, False, True)
    width, height = new_display.get_size()
    
    coordinates=threenp1range(10)
    start = (0,0)
    scale_coordinates={}
    for x,y in coordinates.items():
        scale_coordinates[x*8]=y*8
    print(scale_coordinates.items())
    pygame.draw.lines(screen,"white",False, list(scale_coordinates.items()))
    new_display = pygame.transform.flip(screen, False, True)
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    max_so_far=max(threenp1range(10).values())
    msg = font.render(f"the {max_so_far} is the largest number of iterations", True, "blue")
    new_display.blit(msg, (0,0))
    screen.blit(new_display, (0, 0))
    
    pygame.display.flip()
    pygame.time.wait(1000)
    
    
def main():
   
   dictionary=threenp1range(10)
   graph_coordinates(dictionary)


main()