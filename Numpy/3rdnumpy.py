##### Arrange and Reshape in the Python
import numpy as np 
a = np.arange(24)
print(a)
b = a.reshape(12,2)
print(b)
##### 
a = np.array([1,2,3,4],dtype='i4')
print(f"Size of the memory is {a.itemsize},{a.nbytes}")
b = np.array([1.5,2.5,3.5],dtype=np.float64)
print(b.itemsize)
### Transpose 

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a.T)

### Indexing

a  = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[0,2])

### Indexing in 3d array 
b = np.array([[[1,2,3],[4,5,6]],
               [[7,8,9],[10,11,12]]])
print(b[1,1,2])

### Slicing  in 1d 
one = np.arange(34)
print(one[0:3:1])
### a[2,1:4] it gives the 2 rows from the 1 to 3 values
## same as it gives us if a[1:3,3] the 3 columns from the 1 to 3 values 
#### numpy exmple in the slicing  
import numpy as np 

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[1,1:4])
print(a[1,::-3])
print(a[1,2:4])
print(a[0,0:4])
print(a[1,1:3])