# Program to demonstrate the importance of small value caching. 


a = 100
b = 100

print(a is b)   

x = int("300")
y = int("300")

print(x is y)   

print("ID of a:", id(a))
print("ID of b:", id(b))