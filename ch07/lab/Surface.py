from Rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        
        self.rect= Rectangle(x,y,h,w)
        self.image=filename
        


    def getRect(self):

        """
        
        returns the Rectangle attribute in self.rect
        """
        return self.rect