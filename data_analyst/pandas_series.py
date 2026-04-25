import pandas as pd

s= pd.Series([1,2,3,4,5])
print(s)
# print(type(s))
# print(s.values)
# print(s.index)
# print(s.name)
# s.name = 'My numbers'
# print(s.name)

# indexing

s[0]=10
print(s[0])

print(s[1:4])
print(s.iloc[[0,2,4]])


index=pd.Series(["apple","banana","grapes","orange","strawberry"])
calories=pd.Series([52,89,67,47,33])
calories.name = "Calories"
index.name = "Fruits"
calories.index = index
print(calories)

print(calories.loc[["apple","grapes"]])


# Series Out of dictionary
data = {"apple": 52, "banana": 89, "grapes": 67, "orange": 47, "strawberry": 33}
s2= pd.Series(data)
s2.name = "Calories"
print(s2)


# Conditional selection 
print(s2[s2>50])

# logical operators
print(s2[(s2>50) & (s2<80)])
print(s2[(s2<50) | (s2>80)])
print(s2[~(s2>50)])

# Modifying series

s2["banana"] = 90