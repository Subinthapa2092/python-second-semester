
### set types:: add(), clear(),difference(),differcne_update(), discard(), intersection(),intersection_update(),
### isdisjoint(),issubset(), symmetric_differece(),union(),update()

myset1 = {1,2,3,5,6,12,14}
myset2 = {6,8,5,3,4,9,10}
### generating 0 to 15 set 
print(set(range(0,16,2)))

result = myset1.union(myset2)
print(result)
myset1.update(myset2)###union updated 
print(myset1)
### symmetric_difference 
result2 = myset1.symmetric_difference(myset2)
print(result2)
result2 = myset1.difference(myset2)
print(result2)
### discard :: removing the element from the set 
myset1.discard(14)
print(myset1)
name1 = {"Rakesh Sharma","Rahul Sharma","Subin Thapa","Mahesh Adhikari"}
name2 = {"Rakesh Sharma","Mahima Adhikari","Radha Krishna"}
result = name1.symmetric_difference(name2)
print(result)
### empty 
name = set()
print(type(name))