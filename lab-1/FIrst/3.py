# Program to differentiate an identity and membership operators


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(" Identity Operators ")

print("a is b :", a is b)          # False (different objects)
print("a is c :", a is c)          # True (same object)
print("a is not b :", a is not b)  # True

numbers = [10, 20, 30, 40, 50]

print(" Membership Operators ")

print("20 in numbers :", 20 in numbers)          # True
print("60 in numbers :", 60 in numbers)          # False
print("60 not in numbers :", 60 not in numbers)  # True