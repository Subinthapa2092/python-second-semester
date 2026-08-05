import numpy as np 

data_type = np.dtype([('subject', 'S10'), ('marks', 'i4')])

arr = np.array([('Maths', 90), ('English', 80), ('Science', 85)], dtype=data_type)

### sorting data ordered by subject and marks

sorted_arr = np.sort(arr, order=['subject', 'marks'])
print(arr)
print(sorted_arr)

### numpy.argsort():

a = np.array([90,29,89,12])
print("Orginal array\n",a)
sort_ind = np.argsort(a)
print("Printing indices of sorted dat\n",sort_ind)
sort_a = a[sort_ind]
print("printing sorted array")
for i in sort_ind:
    print(a[i],end = " ")