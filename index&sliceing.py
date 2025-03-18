import numpy as np
import pandas as pd

lables = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print('Labels: ',lables)
print("my data: ",my_data)
print("Dictonary: ",d)

ser1 = pd.Series([1,2,3,4], ['CA', 'OR', 'CO', 'AZ'])
ser2 = pd.Series([1,2,5,4], ['CA', 'OR', 'NV', 'AZ'])

print ("\nIndexing by name of the item/object (string identifier)\n" + "-"*56,sep='')
print("Value for CA in ser1:", ser1['CA'])
print("Value for AZ in ser1:", ser1['AZ'])
print("Value for NV in ser2:", ser2['NV'])

print ("\nIndexing by number (positional value in the series)\n" + "-"*52,sep='')
print("Value for CA in ser1:", ser1[0])
print("Value for AZ in ser1:", ser1[3])
print("Value for NV in ser2:", ser2[2])

print ("\nIndexing by a range\n" + "-"*25)
print ("Value for OR, CO, and AZ in ser1:\n", ser1[1:4],sep='')