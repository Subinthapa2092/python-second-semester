##### inheritance Property 
### syntax 
"""
class Base:
      pass 
class Dervived(Base):
      pass 
"""
### Inheritance Problem:: 

class Room:
    def __init__(self,length,breadth):
        self.length = length 
        self.breadth = breadth
    def getArea(self):
        return (self.length*self.breadth)

class Bedroom(Room):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)### Super automatically implicitely the super to sub
        self.height = height 
    def getvolume(self):
        return (self.length*self.breadth*self.height)
l = int(input("Enter the Length"))
b = int(input("Enter the breadth"))
h = int(input("Enter the height"))
result = Bedroom(l,b,h)
print(result.getArea())
print(result.getvolume())