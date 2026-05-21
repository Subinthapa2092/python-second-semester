##### walrus operator's 
### walrus is an animal just like seal 
## . = where they are eyes and trunk
students = []
while(name:= input("Enter name: ")) != "quit":
    students.append(name)
print(students)
### program to find the
## -real roots, 
## - imaginary roots 
## of a Quadratic equation 
### ax^2+bx+c = 0 
a = float(input("Enter the first terms "))
b = float(input("Enter the second term :: "))
c = float(input("Enter the the constant terms"))
d = b**2-4*a*c 
if d>= 0:
    x1 = (-b+d**0.5)/2*a 
    x2 = (-b-d**0.5)/2*a 
    print("The number is real number's",x1,x2)
else:
    print("The number is imaginary number ")