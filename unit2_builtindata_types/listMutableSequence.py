## it stores the elements of hetorogenous types . It is mutable sequence data type. It is ordered collection of data items. It is denoted by square brackets [ ]. 
# item = [1, 2.5, "Hello", True, [3, 4], (5, 6), {"name": "Alice"}, None]
# print(item)
# print(type(item))

a = []
for i in range(1,21):
    a.append(i)## append  is a function of list call 
## printing the list items 
for i in range(len(a)):
    print(a[i],end = " ")