import numpy as np 

list1 = [1,2,34,5,20,"Subin"]
nar = np.array(list1*5)
print(nar)
print("Type of the nar is ",type(nar))

zeromatrix = np.zeros([2,3,3],dtype = int)
print(zeromatrix)

d = np.eye(5,5,k=0,dtype=int)### you can use k  = -1 ,k = 1 as well
print("\n Matrix a:\n",d)
newarr = np.array([[1,2,3,4],[5,6,7,8]])
trans = np.transpose(newarr)

print(trans)

m = int(input("Enter the value of m "))
n = int(input("Enter the value of n: "))
p = int(input("Enter the value of p : "))
q = int(input("Enter the value of q "))
"""Two matrices are compatible only when n ==p"""

if n == p:
    print("Matrix multiplication is possible.")
    mat1 = []
    mat2 = []
    
    for i in range(m):
        for j in range(n):
            
            print(f"Enter items in mat1[{i}][{j}]")
            mat1[i][j] = int(input("Enter values: "))
            data = int(input("Enter values"))
            mat1.append(data)
            
    for i in range(p):
        for j in range(q):
            print(f"Enter items in mat2[{i}][{j}]")
            mat2[i][j] = int(input("Enter values: "))
            data = int(input("Enter value"))
            mat2.append(data)
    mar1  = np.array(mat1).reshape(m,n)
    mar2 = np.array(mat2).reshape(p,q)
    print(mar1)
    print(mar2) 
    """"lets mutiply the two matrices"""
    product = []
    row_mul_col = 0 
    for i in range(m):
        for j in range(q):
            for k in range(n):
                row_mul_col += mar1[i][k] * mar2[k][j]
            product = row_mul_col 
    final_matrix = np.array(product).reshape(m,q)
    print(final_matrix)
else:
    print("Matrix multiplication is not possible because the number of columns in the first matrix must be equal to the number of rows in the second matrix.")