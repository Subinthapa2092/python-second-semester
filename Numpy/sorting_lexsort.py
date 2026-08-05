import numpy as np
a = np.array(['a','b','c','d','e','f','g'])
b = np.array([15,90,38,12,21,24,67])
ind = np.lexsort((a,b))
print("printing indicez of sorted data")
print(ind)
print("using the indices of sorted data")
for i in ind:
    print(a[i],b[i]) 
    
#### where()

a = np.array([3,2,3,4,8,4,4])
result = np.where(a==4)
print(result)