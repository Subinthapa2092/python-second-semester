#### oop example's 
# class Square():
#     side =  8 
#     def area(self):
#         return self.side**2 

# sq = Square()
# print(sq.area())

# ##### 
# class Area:
#     def __init__(self,side):
#         self.side = side 
    
#     def area(this):
#         return this.side*this.side 
# value = int(input("Enter the number :: "))
# squares = Area(value)## object 

# print(squares.area())    
# #### 
# class Price: 
#     def __init__(self,vat,discount = 10):
#         self.vat = vat 
#         self.discount = discount 
#     def caclculation(self):
#         """Return price after applying vat and fixed discount"""
#         return (self.net_price * (100+ self.vat)/100)- self.discount 
# vat = int(input("Enter the vat amount:: "))
# discount = int(input("Enter the discount amount:: ")) 
# net_price = int(input("Enter the netprice amount : "))
# product  = Price(discount,net_price)
# product.net_price = net_price
# print(product.caclculation())
#### Wap to print the area of recatnagle using class and objects 

class Rectangle:
    def __init__(self,length,breadth,height):
        self.length = length 
        self.breadth = breadth 
        self.height = height
    def calculation_area(self):
        return f"Area of the rectangle is{2*(self.length * self.breadth+self.breadth*self.height+self.length*self.height)}"
    def calculation_volume(self):
        return self.length * self.breadth * self.height
### object 
length = int(input("Enter the length of the recatangle"))
breadth = int(input("Enter the breadth of the rectangle "))
height = int(input("Enter the height of the rectangle "))
area = Rectangle(length,breadth,height)
volume = Rectangle(length,breadth,height)

print(area.calculation_area())
print(volume.calculation_volume())