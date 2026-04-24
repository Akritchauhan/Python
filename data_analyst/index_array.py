import numpy as np

arr1=np.array([1,2,3,4,5])
ind=[0,2]

print(np.take(arr1,ind))

arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for i in np.nditer(arr): 
    print(i,end=" ")

for ind,x in np.ndenumerate(arr):
    print(ind,x)