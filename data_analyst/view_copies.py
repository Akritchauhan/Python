import numpy as np

arr=np.array([1,2,3,4,5])

view=arr[0:3]
print(view)

view[0]=10
print(arr)


# copy

copy=arr[0:3].copy()
print(copy)
copy[0]=20
print(copy)
print(arr)