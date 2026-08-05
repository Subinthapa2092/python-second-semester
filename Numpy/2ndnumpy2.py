#### 
import numpy as np 


a = np.array([1.1,2.1,3.1])
na = a.astype(int)
print(na)
print(na.dtype)
new_conversion = a.astype(bool)
print(new_conversion)

#### Array Attributes::
import numpy as np 
oneD = np.array([1,2,3,4,5])
print(f"Number of the dimension in x: is{oneD.ndim}")
twoD = np.array([[11,12,13,14],[32,33,33,34]])
print(f"Number of dimensions in y : {twoD.ndim}")
threeD = np.array([[[11,12,13,14],[32,33,34,35]],[[55,56,57,58],[59,60,61,62]]])
print(f"Number of dimensions in z : {threeD.ndim}")
