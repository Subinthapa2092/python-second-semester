# ##### 
# """
# wap to find the greastest number among three numbers using nested using nested if else statement 
# [no elif can be used]
# """
# number1 = float(input("Enter the first number :: "))
# number2 = float(input("Enter the second number :: "))
# number3 = float(input("Enter the third number"))
# if number1 > number2:
#     if number1 >number3:
#         maximum = number1
#     else:
#         maximum = number3
# else:
#     if number2 > number3:
#         maximum = number2 
#     else:
#         maximum = number3 
# print("The greatest number among three is maximum",maximum)

### write a program to find the factorial of n positive number 

number = int(input("Enter the number "))
fact = 1
for i in range(1,number+1):
    if number >0:
        fact *= i
        print(fact)
    else:
        print("not a invalid number")
# print(fact)
    