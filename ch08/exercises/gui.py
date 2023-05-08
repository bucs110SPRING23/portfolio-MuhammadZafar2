

class Monster:
  """
  Monster moving across the screen and how the user interacts with
  the monster, whether they hit on the head or body 
  affects life

  """

  def __init(self,touch,touch_on_head,moving):
    self.touch= False  # dead
    self.touch_on_head= True #Alive
    self.moving= 5 #moving 5 blocks back and forth



class Lives(Monster):
  """
  Monster characteristics
  """
  def __init__(self,fall,monster,life_token):
    super().__init__(fall, life_token)    # child class

    self.fall= False #stays alive
    self.life_token=False #gives an extra life
    

class Text():
  
  """
  The details of the text
  
  """
  def _init__(self,font,size,text)
    
    self.font= ""  #font of the text
    self.size= 5  #size of the text
    self.text=input("What is it you seek?")  #Text of the computer

