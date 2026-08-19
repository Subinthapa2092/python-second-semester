# Program to implement the collection module(namedtuple, defaultdict, dequeue chainmap, counter.


from collections import namedtuple, defaultdict, deque, ChainMap, Counter

print("1. namedtuple")

Student = namedtuple('Student', ['roll', 'name', 'marks'])

s1 = Student(1, "Kaushal", 95)

print("Roll :", s1.roll)
print("Name :", s1.name)
print("Marks:", s1.marks)

print("\n2. defaultdict")

d = defaultdict(int)

d['A'] += 1
d['B'] += 2

print(d)

print("\n3. deque")

dq = deque([10, 20, 30])

dq.append(40)        
dq.appendleft(5)     

print("Deque after append operations:", dq)

print("\n4. ChainMap")

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)

print("Combined Dictionary:", cm)
print("Value of b:", cm['b'])

print("\n5. Counter")

text = "python programming"

count = Counter(text)

print("Character Frequency:")
print(count)