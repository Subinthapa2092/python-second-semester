# Program to calculate and print the summation of X= 1 + x3 + 2x2 – 3x3 + 4x4 – 5x5 ……. nxn  using for-else and while-else loops.


# using for-else loop

x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))

sum = 1  

for i in range(1, n + 1):
    if i == 1:
        sum += 3 * x
    elif i == 2:
        sum += 2 * (x ** 2)
    elif i % 2 == 0:
        sum += i * (x ** i)
    else:
        sum -= i * (x ** i)
else:
    print("\nLoop completed successfully")

print("Sum of series =", sum)





# using while-else loop

x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))

sum = 1
i = 1

while i <= n:
    if i == 1:
        sum += 3 * x
    elif i == 2:
        sum += 2 * (x ** 2)
    elif i % 2 == 0:
        sum += i * (x ** i)
    else:
        sum -= i * (x ** i)

    i += 1
else:
    print("\nLoop completed successfully")

print("Sum of series =", sum)