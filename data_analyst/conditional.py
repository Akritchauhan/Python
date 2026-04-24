import numpy as np
a=np.array([1,2,3,4,5])
result=np.where(a<2,"low","High")
print(result)

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.argwhere(b>5))