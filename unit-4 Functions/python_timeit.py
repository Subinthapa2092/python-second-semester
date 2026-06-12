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
def calculate_something(num):
    total = sum((x for x in range(0,num**2)))
    return total 
print(f"And the result is {calculate_something(10)}")
print(f"And the result is {calculate_something(100)}")
print(f"And the result is {calculate_something(1000)}")
print(f"And the result is {calculate_something(10000)}")