import numpy as np
import pandas as pd

lables = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print('Labels: ',lables)
print("my data: ",my_data)
print("Dictonary: ",d)

print(pd.Series(data=my_data))
print(pd.Series(data=my_data,index=lables))
print(pd.Series(arr, lables))
print(pd.Series(d))



