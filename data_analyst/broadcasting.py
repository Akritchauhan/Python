import numpy as np

image=np.array([[200,150],[100,250]])

brightness=image+50
print(brightness)

# Vectorization

def square(x):
    return x**2 

vfunc=np.vectorize(square)
print(vfunc(image))


#dealing with missing values

data=np.array([1,2,np.nan,4,5])
print(np.isnan(data)) #returns a boolean array indicating which values are NaN

#same can be done for np.inf and -np.inf using np.isinf() function

new_data=np.nan_to_num(data) #replaces NaN with 0 and inf with large finite numbers
print(new_data)