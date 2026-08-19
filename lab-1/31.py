# Program to implement the walrus operator.(Write a meaningful program to solve real problems) 



print("Enter numbers (0 to stop):")

while (num := int(input("Number: "))) != 0:

    if num < 0:
        print("Negative number skipped")
        continue

    if num % 2 == 0:
        print("Even number:", num)
    else:
        print("Odd number ignored")

print("Program ended.")