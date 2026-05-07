# # ### 
# # number = float("35") 
# # print(number)
# # print(type(number))

# # import math 
# # r = int(input("Enter the radius of the circle: "))
# # area = math.pi*r*r 
# # circum = math.pi *2*r 
# # print(f"The area of the circle is {area}")
# # print(f"The circumfernce of the circle is {circum}")
# # ### Sphere calculating 
# # total_area = 4*math.pi* r*r 
# # print(f"The total area of the sphere is {total_area}")
# import math 
# number2 = 25.2
# result = math.ceil(number2) ### round up 
# # print(result)
# result1 = math.floor(number2) ## round down 

# print(result)
# print(result1)
# import math as m 
# x = 25 
# y = -34 
# print(math.copysign(x,y))
# # m.copysign(x,y) 
# ## return values of  and by copying the sign of y 
# ### absolute belongs to abs 
# print(abs(y))
# print(m.fsum([1,2,3,4,5,7,8,9,10]))
# # print(m.factorial(5))

# ## recursive function 

# def recursivefunction():
#     number = int(input("Enter the number "))
#     if number <=1:
#         return 1 

#     return number*math.factorial(number-1)
# print(recursivefunction())
### Wap to find the roots of the quaratic equation :: ax^2+bx+c = 0 
# using the math module
import math 
a = int(input("Enter the value of a ")) 
b = int(input("Enter the value of b ")) 
c = int(input("Enter the value of c ")) 
d = b**2 - 4*a*c 
if d > 0:
    root1 = (-b + math.sqrt(d))/(2*a)
    root2 = (-b - math.sqrt(d))/(2*a)
    print(f"The roots are {root1} and {root2}")
elif d == 0:
    root = -b/(2*a)
    print(f"The root is {root}")    
