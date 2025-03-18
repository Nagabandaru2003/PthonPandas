import numpy as np
import pandas as pd


ser1 = pd.Series([1,2,3,4], ['CA', 'OR', 'CO', 'AZ'])
ser2 = pd.Series([1,2,5,4], ['CA', 'OR', 'NV', 'AZ'])
ser3 = ser1 + ser2

print ("\nAfter adding the two series, the result looks like this...\n" + "-"*59,sep='')
print(ser3)

print("\nPython tries to add values where it finds common index name, and puts NaN where indices are missing\n")

print ("\nThe idea works even for multiplication...\n" + "-"*43,sep='')
print (ser1 * ser2)

print ("\nor even for combination of mathematical operations!\n" + "-"*53)
print (np.exp(ser1) + np.log10(ser2))