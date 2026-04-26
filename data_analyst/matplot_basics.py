import matplotlib.pyplot as plt
import pandas as pd

# x=[1,2,3]
# y=[4,5,6]

# plt.plot(x,y)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid()
# plt.show()

# Py plot API

# Univariate - Numerical

data={
    "Salary": [50000, 60000, 70000, 80000, 90000]   
}
df=pd.DataFrame(data)
# line plot
plt.plot(df["Salary"], color="blue", marker="o", linestyle="--")
plt.show()

# Histogram
plt.hist(df["Salary"], bins=5, color="green", edgecolor="black")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")
plt.show()

# Box plot
plt.boxplot(df["Salary"], vert=False)
plt.xlabel("Salary")
plt.title("Salary Box Plot")
plt.show()

# Univariate - Categorical
data={
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"]   
}
df=pd.DataFrame(data)

# pie Chart
count=df["Department"].value_counts()
plt.pie(count, labels=count.index , autopct="%1.1f%% " ,explode=[0.1,0,0,0,0])
plt.title("Department Distribution")
plt.show()

# count plot
plt.bar(count.index, count.values, color="orange")
plt.xlabel("Department")
plt.ylabel("Count")
plt.title("Department Count")
plt.show()

# Bivariate -- Numerical

data={
    "Salary": [50000, 60000, 70000, 80000, 90000],
    "dapartment": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "age": [25, 30, 35, 40, 45]
}

df1=pd.DataFrame(data)
# scatter plot
plt.scatter(df1["age"], df1["Salary"], color="red")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")
plt.show()

# line plot
plt.plot(df1["age"], df1["Salary"], color="blue", marker="o", linestyle="--")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")
plt.grid()
plt.show()

 # Bar Chart
plt.bar(df1["age"], df1["Salary"], color="purple")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")
plt.show()

# Bivariate - Categorical and Numerical

# box plot
plt.boxplot(df1["Salary"], vert=False)
plt.xlabel("Salary")
plt.title("Salary Box Plot")
plt.show()

# pie chart
count=df1["dapartment"].value_counts()
plt.pie(count, labels=count.index , autopct="%1.1f%% " ,explode=[0.1,0,0,0,0])
plt.title("Department Distribution")
plt.show()

# bar chart
plt.bar(count.index, count.values, color="orange")
plt.xlabel("Department")
plt.ylabel("Count")
plt.title("Department Count")
plt.show()

# Multivariate analysis : 3 numerical variables

df1["experience"]=[1,2,3,4,5]

# bubble Plot
plt.scatter(df1["age"], df1["Salary"], s=df1["experience"]*100, color="cyan", alpha=0.5)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary with Experience")
plt.show()

# 2 numerical and 1 categorical variable

plt.scatter(df1["age"], df1["Salary"], color="red")
for i in range(len(df1)):
    plt.text(df1["age"][i], df1["Salary"][i], df1["dapartment"][i], fontsize=9, ha="right")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary with Department")
plt.show()

