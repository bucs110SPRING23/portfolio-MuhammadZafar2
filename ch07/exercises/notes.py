import turtle


#point class an object created from a specific class
#interface: the funcitonsa and variables of an object
#t.forward()# forward()part of the interface if turtle

class Point: 
    # user types always start with a capital letter
    #classes go in their own file
    #1 class per file
    def __init__(self):
        self.x=0
        self.y=0
        self.color=''
    pass
import point

p1=point.Point()
p1.x=10