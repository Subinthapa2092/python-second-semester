
l1 = [2,4,6,8,2,3]
l1.append(10)
print(l1[0:len(l1)])## slicing 
print(f"the number 4 repeated {l1.count(4)} times ")
### alt+ z for wrapping the content
t1 = (11,12,13,14)
l1.extend(t1)
print(l1)
### the different types of method in python list are 
"""
append(), count(),extend(),index(x),insert(index,x),
pop(), remove(),reverse(), sort(),clear(),copy()

"""
l3 = ["Subin Thapa","Hari Adhikari","Mahesh Sharma"]
l4  = l3.copy()
print(l4)
l1.pop()
print(l1)
l1.reverse()
print(l1)
### Bytearryas : it is an built function just like bytes()::

### set types:: add(), clear(),difference(),differcne_update(), discard(), intersection(),intersection_update(),
### isdisjoint(),issubset(), symmetric_differece(),union(),update()