import numpy as np 
a = np.arange(20).reshape(4,5)

print(np.amin(a,axis= 0)) # column axis 
print(np.amin(a,axis = 1)) # row axis 
print(np.amax(a,axis= -1)) ## row axis 
print(np.amin(a)) # minimum in all axes 
print(np.amax(a)) # maximum in all axes