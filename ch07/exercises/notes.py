import turtle


#point class an object created from a specific class
#interface: the funcitonsa and variables of an object
#t.forward()# forward()part of the interface if turtle
# functions are called methods when they are inside a class
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
p2=point.Point()
print(p1.xcoor, p1.ycoor, p1.color, type(p1),id(p1))
print(p2.xcoor, p2.ycoor, p2.color, type(p2),id(p2))

points=[]
for p in range(10):
    x=random.randint(0,100)
    y=random.randint(0,100)
    points.append(point.Point())


def random_color(self):
    new_color



# 
# 
# 
#  

