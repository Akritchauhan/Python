import numpy as np

arr=np.array([1,2,3,4,5,6]) #creates a numpy array from a list of numbers

reshaped=np.reshape(arr,(6,1)) #reshapes the array to a 6x1 array
print(reshaped)

reshaped2=np.reshape(reshaped,(2,3))
print(reshaped2) #reshapes the array to a 2x3 array

ravelled=reshaped2.ravel() #flattens the array back to a 1D array
print(ravelled)

flattened=reshaped2.flatten() #also flattens the array back to a 1D array
print(flattened)

