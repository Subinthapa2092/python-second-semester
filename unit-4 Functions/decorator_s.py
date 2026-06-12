#### Decorator type 


def deco(func): # func = division 
    def inner(a,b):
        if a <b:
            a,b = b, a 
        return func(a,b)
    return inner 

@deco 
def Divide(x,y):
    return x/y 

print(Divide(5,7))
print(Divide(10,2))
### deccorator is a function that changes the behaviour of another 
### function without modifying it . 
### Class Task: 
### Create a decorator function that is used to decorate the factorial 
### function such that the negative number 
### becomes postive after using the decorator 
import math
def deco(func):
    def inner(n):
        if n <0:
            n = math.fabs(n)
            return func(n)
        return inner
@deco
def factorial(n):
    if n<= 1:
        return 1
    return n*math.factorial(n-1)
print(factorial(5))
            