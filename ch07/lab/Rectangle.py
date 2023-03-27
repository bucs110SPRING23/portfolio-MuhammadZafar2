class Rectangle:
    def __init__(self,x,y,height,width):
        self.x=abs(x)
        self.y=abs(y)
        self.width=abs(width)
        self.height=abs(height)


    def __str__(self):
        
        return self.x, self.y, self.height, self.width