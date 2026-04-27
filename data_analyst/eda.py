import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sms   

df=pd.read_csv("dataset/heart.csv")
print(df.head())
print(df.info())
print(df.shape())
print(df.describe()) #statistical summary



