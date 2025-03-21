import numpy as np
arr1 = np.array([[4, 7], [2, 6]], 
                 dtype = np.float64)
                  
arr2 = np.array([[3, 6], [2, 8]], 
                 dtype = np.float64) 

Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)
Sum1 = np.sum(arr1)
print("\nAddition of Array elements: ")
print(Sum1)

Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)

Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)