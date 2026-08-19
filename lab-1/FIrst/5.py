# Program to convert the decimal number into binary form. 

decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)

print("Binary form =", binary[2:])