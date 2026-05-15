#### python in a program to do the menu driven program using 
### the match statment :: 
### showing the 
"""
1) add
2) subtract 
3) Divide 
4) Multiply 
5) remove

"""
choice = input("Enter your choices (add,sub,mul,div,rem): ")
number1 = int(input("Enter the first integer number "))
number2 = int(input("Enter the second number:: "))

match(choice):
    case "add":
        print("Addition",number1+number2)
    case "sub":
        print("Subtraction",number1-number2)
    case "mult":
        print("Multiplication",number1*number2)
    case "div":
        if number2 != 0:
            print("Divisition",number1/number2)
        else:
            print("Not divisible by zero")
    case "rem":
        print("Remainder",number1 % number2) 

print("Program executed succesfully ! ")   