import numpy as np #alias for numpy

arr=np.array([1,2,3]) #creates a numpy array from a list of numbers

print(arr.ndim)

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]]) #creates a 2D array from a list of lists 
print(arr1.ndim)

arr2=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]) #creates a 3D array from a list of lists of lists
print(arr2.ndim)
