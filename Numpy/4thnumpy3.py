### Python in a program to do the numpy work 
import numpy as np 
arr = np.array([1,2,3,4,5])
# arr[0] = 42
x = arr.copy()
arr[0] = 59
print(arr)
print(x)
print("But View make the change in both arrays")
y = arr.view()
arr[0] = 57
print(arr)
print(y)