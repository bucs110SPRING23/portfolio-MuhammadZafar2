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
    print(objs_in_sequence)


def main():
    threenp1range(10)

# if __name__ == "__main__":
main()





def graph_coordinates(objs_in_sequence):
    screen = pygame.display.set_mode((690,690))
    new_display = pygame.transform.flip(screen, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
    #new_display=pygame.Surface.blit(new_display,)
    pygame.display.flip()
    coordinates=threenp1range(10).objs_in_sequence.items()
    pygame.draw.lines(new_display,"white",False,coordinates)
    max_so_far=max(coordinates.values())

graph_coordinates(threenp1range)
