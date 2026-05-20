##write a python to calculate the binary representation for numnber
n = 39 
remainders = []
while n > 0:
    remainder = n%2 
    remainders.append(remainder)
    n //= 2 
remainders = remainders[::-1]
print(remainders)
### Write a python script to enter the names of students(unlimited) unitll you enter the 
## you enter the string values "thatsit"
### using while loop::

name_list = []
while True:
    name = input("Enter the name of the person ")
    if name == "thatshit":
        print(name)
        break 
    else:
        name_list.append(name)
print("Program ended ")
for i in range(len(name_list)):
    print(i,name_list[i])