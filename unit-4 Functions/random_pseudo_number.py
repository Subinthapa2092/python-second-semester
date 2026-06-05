### python in a program to do the random number generator 
# #### pseudo random numbers 
# from random import random,seed, randint,uniform,choice,randrange
# print(random()) ### generate random number 
# # seed(1)### repeat the same random number number
# print(random())
# print(random())
# ## choice the function's 
# print(choice("abcdefghijklmnopqrstuvwxyz"))
# print(choice(range(10)))
# # x = int("Enter the first number : ")
# # # print(seed(x))
# # print(random.seed(5))
# # print(random.sample([5,10,30],5))

# random.seed(9)
# print(random.random())
# import random 
# random.seed(5)
# print(random.random(5))
# print(random.random(5))
### two used the decorator 's 

students = [
    dict(name = "Ram",credits = dict(math = 90,physics = 64,history= 99)),
    dict(name = "Harrendra",credits = dict(math= 99,physics = 79,latin = 44)),
    dict(name = "Ramhari",credits = dict(math = 90,physics = 64,history= 99)),
    dict(name = "Arya",credits = dict(math= 99,physics = 79,latin = 44)),
]

def decorators(s):
    return (sum(s["credits"].values()),s)

# students = sorted(map(decorators,students))
# print(students)
## sorting 
students = sorted(students,key = decorators)
print(students)
### sorting with mapped 
students = sorted(students,key = lambda s: sum(s["credits"].values()))
print(students)
    