
#### learning the Arithmetica OPerator 
## +,-,/,*,% ,//,**

a = int(input("Enter the First number :: "))
# b = int(input("Enter the second number:: "))
if a % 2 == 0:
    print(str(a) + "  is Even number")
else:
    print(str(a) + " is Odd number")

### like composite :: divisible by multiple number 
count = 0 
for i in range(2,a+1):
    if a % i == 0:
        
        count = count + 1
if count == 2 :
    print(str(a) + "is a prime number")
else:
    print(str(a) + "is a composite number")