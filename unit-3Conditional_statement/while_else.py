# ### a program to find the sum of the squares of numbers from 1 to n (1^2+2^2+3^2+...+)
# num = int(input("Enter a numbers:: "))
# sum = 0 
# while (num>=1): ### 5 
#     sum = sum+num**2 ## for the pow(num,2)
#     print(num**2)
#     num -= 1 
# else:
#     print(f"{num} is no more greater or equals to 1")
# print("Sum of the squares = "+str(sum))
### second question's 
### wap to find the summation of the following series using while-else 
### x = 1+y^2-3y^3+4y^4-5y^5+.....ny^n 
## solution 
n = int(input("Enter any no. of terms:: "))
y = int(input("Enter the value of Y::"))
x = 1 + y**2 ###initial value of summation x 
while n>= 3:
    x = x+(-1)**n*n*y**n 
    n -= 1 
else:
    print(f"X = {x} is nor more greater than 1 ")
print(f"X ={x}")
""""
while n>=1:
if n%2 == 0:
x = x+ n*y**n ## or replace y**n with math.pow(y,n)
else:
x = x-n*y**n
"""
### Harmoni series :: 
yes = "yes"
while yes == "yes":
    sum = 0 
    n = float(input("Enter terms:: "))
    while n>=1:
        sum = sum+1/n 
        n -= 1 
    else:
        print(f"{n} is less than 1")
    print(f"Sum = {sum}")
    print("Do you wish to continue\n")
    yes = input("Enter yes for continue no for discontinuity\n")
else:
    print("User disrupts the flow of a program\n")        