import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)

b = np.array([[1,2,3,4],[1,2,3,4]])
print(b)

print(a.ndim) #dimensions
print(b.ndim)

print(b.shape) # show rows and columns

print(b.dtype) # shows data type

print(a.itemsize)
print(a.nbytes)

c = np.array([[1,2,3,4],[1,2,3,4]])
