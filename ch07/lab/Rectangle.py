class Rectangle:
    def __init__(self,x,y,height,width):
        self.x=abs(x)
        self.y=abs(y)
        self.width=abs(width)
        self.height=abs(height)


    def __str__(self):
        """
        returns a string containing the x, y, width, and height of the rectangle. 
        
        """
        return self.x, self.y, self.height, self.width