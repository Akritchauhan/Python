import numpy as np

a=np.array([1,2,3,4,5]) #creates a numpy array from a list of numbers
b=np.array([6,7,8,9,10]) #creates another numpy array from a list of numbers

print(a+b) #performs element-wise addition of the two arrays
print(a-b) #performs element-wise subtraction of the two arrays
print(a*b) #performs element-wise multiplication of the two arrays
print(a/b) #performs element-wise division of the two arrays
print(a**2) #performs element-wise exponentiation of the array
print(np.add(a,b)) #performs element-wise addition using numpy's add function
print(np.subtract(a,b)) #performs element-wise subtraction using numpy's subtract function
print(np.multiply(a,b)) #performs element-wise multiplication using numpy's multiply function
print(np.divide(a,b)) #performs element-wise division using numpy's divide function
print(np.power(a,2)) #performs element-wise exponentiation using numpy's power function
print(a%2) #performs element-wise modulus operation on the array

