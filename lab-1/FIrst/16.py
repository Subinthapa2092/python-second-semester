#  Program to implement any ten methods in set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)


set1.add(10)
print("\n1. After add(10):", set1)


set1.remove(2)
print("2. After remove(2):", set1)


set1.discard(20)  
print("3. After discard(20):", set1)


removed_item = set1.pop()
print("4. After pop():", set1)
print("   Popped element:", removed_item)


union_set = set1.union(set2)
print("5. Union of set1 and set2:", union_set)

 
intersection_set = set1.intersection(set2)
print("6. Intersection of set1 and set2:", intersection_set)


difference_set = set1.difference(set2)
print("7. Difference of set1 and set2:", difference_set)


sym_diff_set = set1.symmetric_difference(set2)
print("8. Symmetric Difference:", sym_diff_set)


subset_check = {4, 5}.issubset(set2)
print("9. Is {4,5} subset of set2?:", subset_check)


temp_set = {100, 200, 300}
print("10. Before clear():", temp_set)

temp_set.clear()
print("    After clear():", temp_set)