import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "Salary": [50000, 60000, 70000, 80000, 90000]
}
df=pd.DataFrame(data)
print(df)
print(df.head(2))
print(df.tail(2))

#loc and iloc
print(df.iloc[0:2])
print("")
print(df.loc[0:2,["Name","City"]]) # print index 0,1,2 with col name and city

df.drop("Department", axis=1,inplace=True) # drop the column department
print(df)

print(df.shape)
print(df.info())
print(df.describe())

# Broadcasting
df["Salary"] = df["Salary"] * 1.1 # increase salary by 10%
print(df)

# Renaming columns
df.rename(columns={"Name": "Employee Name", "Age": "Employee Age"}, inplace=True)
print(df)

df["department"] = ["HR", "Finance", "IT", "Marketing", "Sales"]
print(df["department"].value_counts()) 


# Data Cleaning
print(df.isnull().sum() )# check for null values
df.dropna(inplace=True) # drop rows with null values
df.fillna(0, inplace=True) # fill null values with 0
df["department"]=df.fillna(df["department"].mode()[0]) # fill null values with mode of department column
df.fillna(method="ffill", inplace=True) # forward fill null values
df.fillna(method="bfill", inplace=True) # backward fill null values

df_d=df.duplicated() # check for duplicate rows
print(df_d)
df.drop_duplicates(inplace=True) # drop duplicate rows 

# Invalid data
#lambda function to check for negative salary
df["Salary"] = df["Salary"].apply(lambda x: x if x >= 0 else 0) # set negative salary to 0
print(df)

#apply and lambda function
df["Age Group"] = df["Employee Age"].apply(lambda x: "Young" if x < 30 else "Middle-aged" if x < 40 else "Senior")
print(df)

#joins and merges 
data1 = {
    "Employee Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Project": ["Project A", "Project B", "Project C", "Project D", "Project E"]
}
df1 = pd.DataFrame(data1)
merged_df = pd.merge(df, df1, on="Employee Name", how="inner")

#import file

# df = pd.read_csv("file.csv")