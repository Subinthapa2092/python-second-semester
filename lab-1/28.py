#  Write a program using match statement to develop a simple calculator for +, -, *, /, and % operators. 


a,b = map(float, input("Enter two number: ").split())
op = input("Enter operator (+, -, *, /, %): ")

match op:
    case "+":
        print("Result =", a + b)

    case "-":
        print("Result =", a - b)

    case "*":
        print("Result =", a * b)

    case "/":
            print("Result =", a / b)

    case "%":
            print("Result =", a % b)
            
    case _:
        print("Invalid operator")