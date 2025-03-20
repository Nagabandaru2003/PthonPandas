import numpy as np

arr1d = np.array([10,20,30,40,50])
print('single element in any indexing array : ',arr1d[2])
print('negative index: ',arr1d[-1])

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('mul dimentional array: ',arr2d[1,0])

print(arr1d[1:4])
print(arr1d[2:])