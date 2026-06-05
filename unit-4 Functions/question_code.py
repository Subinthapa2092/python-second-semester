#### python in a program to do the 
#### (1_x^3 )+ 2_x^2 - 3_x^3 + 4x^4 - ....... nx^n 
import math 
n = int(input("Enter the value of x (terms): ")) 
y = int(input("Enter the value of y : "))
sum = 1+pow(n,3)
# 
while y > 1:
    sum += math.pow(-1,n)*n*math.pow(y,n)
   
    n = n-1
print(f"The sum of the series is {sum}")
### 