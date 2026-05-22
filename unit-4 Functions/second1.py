#### program to find the factorial of the number 


def factorial(n):
    fact = 1 
    for i in range(1,n+1):
        fact *= i
    return fact
n =int(input("Enter the number N : "))
r = int(input("Enter the enter r"))
cnr = factorial(n)/factorial(n-r)*factorial(r)
print(f"The combination of the factorial is {cnr}")