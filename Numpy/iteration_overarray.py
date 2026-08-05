import numpy as np 

arr = np.array([[[1,2],[3,4],[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)


### Sorting and Searching in Python's 

# Quick Sort, Merge Sort, and heapsort 

a = np.array([[12,6],[10,11],[16,14]])
arr1 = np.sort(a,kind= "mergesort",axis = 1) # it sorts iteam in decending
arr2 = np.sort(a,kind= "headsort",axis = 0)## i
arr3 = np.sort(a,kind= "quicksort",axis = 1)##
arr4 = np.sort(a,kind= "quicksort",axis = None)#it sorts all the items

print(arr)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(np.sum(arr1,axis= -1))### sum over last dimension 
print(np.sum(arr1,axis = 1))## sum over column
print(np.sum(arr1,axis=0))## sum over row