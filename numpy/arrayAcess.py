import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array([[1,2,3,4],[1,2,3,4]])
c = np.array([[1,2,3,4,5,6,7,8],
              [1,2,3,4,5,6,7,8]])
print(c)

print(c[1,2])#(r,c)

print(c[:,2])#total call specific

d = np.array([[[1,2],[2,3],[3,4],[5,6]]])
print(d)

print(d.ndim)

s= np.zeros((2,3))
print(s)

p = np.ones((2,3,4))
print(p)

q = np.full((2,3),99)
print(q)

r =np.random.rand(4,2)
print(r)

c= np.identity(s)
print(c)