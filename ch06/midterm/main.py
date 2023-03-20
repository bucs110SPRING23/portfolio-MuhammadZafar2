import turtle


def draw_handle(turtle,length,width):
    """

    Makes the handle of the lollipop
    turtle object used to draw
    length parameter (float) is the length of handle 
    width parameter (float) is a width of handle
    returns (float) the length and width parameter
    
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
    draw_circle is made to make the lollipop candy using draw_handle function
    turtle  : used to draw
    handle_length/_width (float) is the returned value from draw_handle
    radius (float) is added to make circle
    
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
    this function just combines the draw_circle and draw_handle functions to make the whole lollipop
    length, width, radius (float) inputed to build the whole lollipop
    
    
    """
    handle_dimensions=draw_handle(turtle,length,width)  
    handle_width=handle_dimensions[1]
    handle_length=handle_dimensions[0]/2
    draw_circle(turtle,handle_length, handle_width,radius)


def main(length,width,radius):                             
    
    window = turtle.Screen()   
    window.bgcolor('lightblue')
    draw_lollipop(length,width,radius)
    window.exitonclick()

main(50,100,50)