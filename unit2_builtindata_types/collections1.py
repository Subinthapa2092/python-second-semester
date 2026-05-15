#### Collection Module in Python's 
import collections as col
employee = col.namedtuple("employee",("name","age"))
em1 = employee("subin Thapa",19)
print(em1.age)
print(em1[1])
#### deque 

numbers = col.deque([],maxlen= 6 )
for i in range(10):
    numbers.append(i)
print(numbers)
### Counter 
from collections import Counter 
# c = counter()
list = [1,2,3,4,5,7,9,9,7,7,7]
c = Counter(list)
print(Counter(list))
c1 = c.values()
print(c1)
mode_value = max(c1)
print(mode_value)
## modes using python 
c = Counter(list)
mode_value = max(c.values()) 
print(mode_value) 
## finding the higgest repeated values(modes values)
s1 = [1,2,3,4,5,7,9,9,7,7,7]
c = Counter(s1)
mode_value = max(c.values())
mode = [k for k,v in c.items() if v == mode_value]
print(mode)
### without using the default dit 
quote = "nothing is permanent in life besides non living things"
d = {}
for i in quote:
    if i not in d:
        d[i] = 0
    else:
        d[i] += 1 
print(d)
### using the deafault dict:: 
from collections import defaultdict 
quote = "nothing is permanent in life besides non living things"
d = defaultdict(int) 
for i in quote:

   d[i]+=1
print(d)

def getaddress():
    return "Dhading"
student = {"Name":"Subin Thapa","age":19}

student = defaultdict(getaddress)
print(student["country"])
#### updating values in the python :: 
student["age"] = 20 
print(student)
a = 50 
b = 501
print(id(a) == id(b))
a = 1000 
b = 1000 
print(id(a) == (id))