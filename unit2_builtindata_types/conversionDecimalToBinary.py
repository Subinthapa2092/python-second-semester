#### Wap to convert the decimal number into binary from 
num = int(input("Enter any number :: "))
tem = num
remainderlist = []
while num != 1:
    a = num % 2 
    remainderlist.append(a)
    num //= 2 ## integer division we use // operator but here we are using / operator because we want to get the quotient in float form and we will convert it into integer in the next step
    num = int(num) ## converting the quotient into integer form 
print(f"The binary form of {tem} is given below ")
print(remainderlist[::-1])

### program in a python to check the palindrome or not 
number = int(input("Enter the first number :: ")) 
original = number
sum  = 0 
while number != 0:
    digit = number % 10
    sum = sum * 10 + digit
    number = number// 10
    
if sum == original:   
    print("The number is  palindrome")
else:   
    print("The number is not palindrome")
    