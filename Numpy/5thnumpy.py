##### Python Code:: linespace

import numpy as np 

x = np.linspace(10,20,15,True,False,dtype=int)### endpoint = true retstep is true
y = np.linspace(10,20,5,True,True,dtype=float)
print(x)
print(y)
### logspace

a = np.logspace(1,10,num =10 ,base = 2,dtype=float)
print(a)
### Array broadcasting 

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a*b 
print(c)

num1 = np.array([[1,2,3,4],[2,4,6,8]])
num2 = np.array([[10,20,30,40],[1,2,3,4]])
c = num1*num2 
print(c)