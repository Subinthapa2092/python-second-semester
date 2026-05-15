# #### python in a program to do the find the summation of n natural number 

# number = int(input("Enter the number:: "))

# sum = 0 
# for i in range(number+1):
#     sum += i
# print(sum)
# ### fibonnic series 
# a,b = 0,1 
# print(f"{a}\n{b}")
# for i in range(2,number+1):
#     c = a+b 
#     print(f"{c}")
#     a,b = b,c 
### sum of the series:: sum = a+ax+ax^2+ax^3+......ax^n 
number = int(input("Enter the number :: "))
a = int(input("Enter the number a")) 
x = int(input("Enter the values of the x: "))
# sum = 0
import math 
if number >0:
    sum = 0 
    for i in range(number):
        sum = sum + a* math.pow(x,i)
else:
    print(f"{number} is negative")
print(sum)