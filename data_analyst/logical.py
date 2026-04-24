import numpy as np
a=np.array([1,2,3,4,5])
mask=np.logical_and(a>2,a<5)
print(mask)
mask1=np.logical_or(a<2,a>4)
print(mask1)