def Factorial(n):
    if n == 0 or n ==1:
        return 1 
    return n*Factorial(n-1)

def fibonacci(n):
    if n == 0 or n ==1:
        return n 
    return fibonacci(n-1)+fibonacci(n-2)
if __name__ == '__main__':
    
    n = int(input("Enter n : "))
    print(f"The factorial of n is {Factorial(n)}")
    print(f"The fibonacci of n is ")
    for i in range(n):
        print(fibonacci(i),end = " ")