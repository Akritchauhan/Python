import numpy as np

arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr.T)
print(arr.transpose())

arr1=np.array([[[1, 2], [3, 4], [5, 6]]])
print(arr1.shape)

swap=np.swapaxes(arr1,0,2)
print(swap.shape)

# concatination

a=np.array([1,2])
b=np.array([3,4])
print(np.concatenate((a,b)))

# spliting of array
print(np.split(arr,3))
print(np.hsplit(arr,3))
print(np.vsplit(arr,3))