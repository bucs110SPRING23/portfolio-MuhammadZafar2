import turtle


def draw_handle(turtle,length,width):
    """

    Makes the handle of the lollipop
    turtle object,used to draw
    length parameter is the length of handle 
    width parameter is a width of handle
    returns the length and width parameter
    
    """
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    return length , width

def draw_circle(turtle,handle_length,handle_width,radius):
    """
    turtle object used to draw
    handle_length/_width is the returned value from draw_handle
    radius is added
    
    """
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(handle_length,handle_width)
    turtle.pendown()
    
    turtle.circle(radius)
    turtle.end_fill()
    x=1
    for i in range(30):
        turtle.left(15*x)
        turtle.forward(15)
        x+=.09

    


def draw_lollipop(length,width,radius):

    """
    length, width, radius imputed to build the whole lollipop
    
    
    """
    handle_dimensions=draw_handle(turtle,length,width)  #is it okay to hard code it or ask the user?
    handle_width=handle_dimensions[1]
    handle_length=handle_dimensions[0]/2
    draw_circle(turtle,handle_length, handle_width,radius)


def main(length,width,radius):                             #can we put parameters in main
    
    window = turtle.Screen()   #Create a screen
    window.bgcolor('lightblue')
    draw_lollipop(length,width,radius)
    window.exitonclick()

main(50,100,50)