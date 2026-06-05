# #### Without the list comprehesion 
# employee = ["Naresh",'Saubhagya',"Haresh","Subin","arya Phuyal"]
# list1 = []
# for i in employee:
#     if "arya Phuyal" in i:
#         list1.append(i)
# print(list1)
# ### wap to print the multiplication table of n 
# n = int(input("Enter the values of n : "))
# terms = int(input('Enter the terms '))
# mlist = []
# mlist = [n*i for i in range(1,terms+1)]
# print(mlist)
#### program in a python to print the multiplication of the table 

# n = int(input("Enter the number ::: "))
# terms = int(input("Enter the terms :: "))
# for i in range(1,n+1):
#     for j in range(1,terms+1):
#         print(f"{i}*{j} = {i*j}")
#     print()
# new_list = [f"{i}*{j} = {i*j}" for i in range(1,n+1) for j in range(1,terms+1)]
# print(new_list)
#### Filter Comprehension 
from math import sqrt 
 
mx = 10 
legs = [(a,b,sqrt(a**2 + b**2)) for a in range(1,mx) for b in range(a,mx)]
legs = list(filter(lambda triple : triple[2].is_integer(),legs))
print(legs)
