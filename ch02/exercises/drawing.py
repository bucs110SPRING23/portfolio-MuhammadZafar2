import turtle
window= turtle.Screen()
sides= int(input("How many sides would you like?: "))
length= int(input("How long would you like it?: "))

mike= turtle.Turtle()

mike.color("green")


for i in range(sides):
    mike.forward(length)
    mike.left(360/sides)
    i+=1



window.exitonclick()