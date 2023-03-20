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
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
    
    coordinates=threenp1range(10).items()
    start = (0,0)
    for coord in coordinates:
        pygame.draw.lines(new_display,"white",False, [start, coord])
        start=coord
    
    screen.blit(new_display, (0, 0))
    pygame.time.wait(1000)
    # pygame.display.flip()
    max_so_far=max(threenp1range(10).values())
    # pygame.font.init()
    # font = pygame.font.Font("italic", 12)
    # msg = font.render(f"the {max_so_far} is the largest number of iterations", antialias, "blue")
    # display.blit(msg, (0,0))

graph_coordinates(threenp1range(10))


# def graph_coordinates(objs_in_sequence):
#    coordinates=objs_in_sequence.items()


def main():
   threenp1()
   dictionary=threenp1range(10)
   graph_coordinates(dictionary)