
import numpy as np
import pandas as pd
from numpy.random import randn as rn

np.random.seed(101)
matrix_data = rn(5,4)
row_labels = ['A','B','C','D','E']
column_headings = ['W','X','Y','Z']

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nThe data frame looks like:\n" , "-"*45, sep='')
print(df)

print("\nThe 'X' column:\n", "-"*25, sep='')
print(df['X'])
print("\nType of the column:", type(df['X']), sep='')

print("\nThe 'X' and 'Z' columns Indexed by passing a list:\n", "-"*55, sep='')
print(df[['X', 'Z']])
print("\nType of the pair of columns:", type(df[['X', 'Z']]), sep='')
print("\nSo, for more than one column, the object turns into a DataFrame")