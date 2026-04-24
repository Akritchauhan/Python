import numpy as np

a=np.array([1,2,3,4,5])
print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a)) 
print(np.min(a))
print(np.max(a))


matrix=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.sum(matrix,axis=1)) #sum of each column
print(np.sum(matrix,axis=0)) #sum of each row