import matplotlib.pyplot as plt
import pandas as pd

data={
    "Salary": [50000, 60000, 70000, 80000, 90000],
    "Age": [25, 30, 35, 40, 45],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"]
}
df=pd.DataFrame(data)

fig, ax = plt.subplots(1,3, figsize=(15,5))

#Line plot
ax[0].plot(df["Age"], df["Salary"], color="blue", marker="o", linestyle="--")
ax[0].set_xlabel("Age")
ax[0].set_ylabel("Salary")
ax[0].set_title("Age vs Salary")
ax[0].grid()

# histogram
ax[1].hist(df["Salary"], bins=5, color="green", edgecolor="black")
ax[1].set_xlabel("Salary")
ax[1].set_ylabel("Frequency")
ax[1].set_title("Salary Distribution")

# box plot
ax[2].boxplot(df["Salary"], vert=False)
ax[2].set_xlabel("Salary")
ax[2].set_title("Salary Box Plot")
plt.tight_layout()
plt.show()

# many plots in one figure

data2={
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "Count": [10, 20, 15, 25, 30],
    "years": [5, 10, 15, 20, 25],
    "Salary": [50000, 60000, 70000, 80000, 90000],
}
df2=pd.DataFrame(data2)
plt.plot(df2["years"], df2["Salary"], color="blue", marker="o", linestyle="--")
plt.plot(df2["years"], df2["Department"], color="red", marker="o", linestyle="--")
plt.plot(df2["years"], df2["Count"]*1000, color="green", marker="o", linestyle="--")
plt.xlabel("Years")
plt.ylabel("Salary/Department/Count")
plt.title("Years vs Salary/Department/Count")
plt.legend(["Salary", "Department", "Count"])
plt.grid()
plt.show()

# 3-D plot

ax=plt.axes(projection="3d")
ax.scatter(df2["years"], df2["Salary"], df2["Count"], color="blue", marker="o")
ax.set_xlabel("Years")
ax.set_ylabel("Salary")
ax.set_zlabel("Count")
ax.set_title("3D Scatter Plot")
plt.show()
