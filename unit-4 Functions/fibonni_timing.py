#### Time it function's 
import time
def timeit(func):
    def timeit_inner(number):
        start_time = time.time()
        result = func(number)
        end_time = time.time()
        total_time = end_time - start_time 
        print(f"Function {func.__name__} without parameter {number} took {total_time:.4f} seconds")
        return result 
    return timeit_inner

@timeit 
def fibonnic(n):
    a, b = 0, 1
    sums = 0 
    for i in range(3,n+1): 
        c = a+b 
        a,b = b,c
        sums += c 
    return sums 
# n = int(input("Enter the number : "))
print(f"Fibonaci of number {fibonnic(10)}")
print(f"Fibonaci of number {fibonnic(100)}\n")
print(f"Fibonaci of number {fibonnic(1000)}\n")