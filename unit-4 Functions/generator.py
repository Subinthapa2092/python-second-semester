# # # #### 
# # # name = {}
# # # print(type(name))
# # # name = set()
# # # print(type(name))
# # ### Topics:: Generator with yields and next 

# # def get_squares(n):
# #     return [x**2 for x in range(n)]
# # print(get_squares(10))
# # #### generator with next(),yeilds:: 

# # def get_square(n):
# #     for i in range(n):
# #         yield i**2 
# # n = int(input("enter the number:: "))
# # result = get_square(n)
# # print(next(result))
# # print(next(result))
# # print(next(result))
# # print(next(result))

# ## using generators 
# def getcube(n):
#     for i in range(n):
#         yield pow(i,3)
        
# result = getcube(100)
# # print(next(result))
# # print(next(result))
# # print(next(result))
# clist = []
# clist.append(next(result))
# clist.append(next(result))
# print(clist)

# def fibonacci():  or def fibonacci(n):
#     a, b = 0, 1
#     while True:  or while a<=n
#         yield a
#         a, b = b, a + b

# gen = fibonacci()
# for i in range(10):
#     print(next(gen))
# def fibonacci(n):
#     a,b=0,1
#     while a<=n:
#         yield a 
#         a,b = b, a+b
# n=int(input("enter a number:"))
# result = fibonacci(n)
# # print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# for i in range(n):
    # print(f"{1+1/(next(result))}")
def harmonic(n):
    sum = 0 
    for i in range(1,n+1):
        yield sum +1/i 
result = harmonic(10)
print(next(result))
print(next(result))
print(next(result))
    