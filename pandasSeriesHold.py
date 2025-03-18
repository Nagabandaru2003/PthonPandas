import numpy as np
import pandas as pd

lables = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print('Labels: ',lables)
print("my data: ",my_data)
print("Dictonary: ",d)

print('\nholding numerical data\n','_'*25,sep='')
print(pd.Series(arr))
print('\nholding text labels\n','_'*20,sep='')
print(pd.Series(lables))
print('\nholding functions\n','_'*20,sep='')
print(pd.Series(data=[sum,print,len]))
print('\nholding objects from a dictionary\n','_'*40,sep='')
print(pd.Series(data=[d.keys,d.items,d.values]))


