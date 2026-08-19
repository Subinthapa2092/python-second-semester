# Program to find the even numbers from 1 to 100 using list sequence.


even_numbers = []

for number in range(1, 101):
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers from 1 to 100 are:")
print(even_numbers)