#### Operator Overloading in Python

class Point:
    def __init__(self,x=0,y= 0):
        self.x = x 
        self.y = y 
    
    def __add__(self,other):### Operator Overloading
        t1 = self.x + other.x 
        t2 = self.y + other.y
        return t1,t2
    def __str__(self):### built in function 
        return "(0,1)".format(self.x,self.y)
point1  = Point(2,5)
point2  = Point(5,8)
point3  = point1 +point2 ### it's call the function point1.__add__(point2)
print(point3)

