# ### program in a python to do the recursive function work'
# ## Calculating the recursive function for factorial 
# def factorial(n):
#     if n == 0: ## base case or ## if n in (0,1)
#         return 1
#     return factorial(n-1)*n ## recursive case
# number = int(input("Enter number for factorial: "))
# print(f"The factorial number is {factorial(number)}")
# ### wap to find the fibonacci series upto n 



# def fibonacci(a):
#     if a in (0,1):
#         return a 
#     return fibonacci(a-1)+fibonacci(a-2)
# terms = int(input("Enter the no. of the terms:: "))
# for i in range(terms):
#     print(fibonacci(i),end = " ")
    
### wap fo find the power(a,b) i.e a^b 

# def Power_number(a,b): ## 1,2 
#     if a == 0:
#         return 0 
#     elif b == 0:
#         return 1
#     elif b >0:
#         return a*Power_number(a,b-1)
#     else:
#         return (1/a)*Power_number(a,b+1)

x = int(input("Enter the first number :: "))
y = int(input("Enter the second number:: "))
# print(f"The power of {x,y} is {Power_number(x,y)}")
### wap to find the greatest common divisior gcd(x,y)    

def GCD(x,y):
    if x % y == 0:
        return y 
    return GCD(y,x%y)
print(f"The GCD of {x,y} is {GCD(x,y)}")