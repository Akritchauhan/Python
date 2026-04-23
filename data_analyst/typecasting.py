import numpy as np

arr=np.array([1,2,3,4,5]) #creates a numpy array from a list of numbers

new_arr=arr.astype(np.float64) #typecasting the array to float64

arr2=np.array([[1,2,3],[4,5,6],[7,8,9]]) #creates a 2D array from a list of lists

print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.size)
print(arr2.itemsize)