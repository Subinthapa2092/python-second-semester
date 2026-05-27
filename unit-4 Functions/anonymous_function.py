#### python in a program ]
### using user defined function i.e not annoymous 

# def is_mulitiple_of_five(n):
#     return not n% 5 

# def get_multiple_of_five(n):
#     ## filter(function,iterables)
#     return list(filter(is_mulitiple_of_five,range(n)))
# n = int(input("Enter the numbers:: "))
# print(get_multiple_of_five(n))
# ## using the lambda function 
number = int(input("Enter the number "))
def get_lambda_function(n):
    return list(filter(lambda x: not x % 5,range(n)))
print(get_lambda_function(number))