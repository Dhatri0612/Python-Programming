import pandas as pd
csv_1=pd.read_csv("C:\\Users\\USER\\OneDrive\\Desktop\\test.csv")
print(csv_1)
print(csv_1.index)
print(csv_1.columns)
print(csv_1.describe())
print(csv_1.head())  # ye starting k 5 row ko de dega data k
print(csv_1.head(2))  # ab ye starting k bs 2 row ko dega
print(csv_1.tail())  # ye niche se 5 row ko de dega
print(csv_1.tail(2))  # ab ye niche k bs 2 row ko dega
print(csv_1[6:11])  # ye 6 se 10 tk print krega by using slicing
print(csv_1.index.array)  # ye index ki array bnaa deta h 
print(csv_1.to_numpy())  # ye numpy array bnaa deta h
import numpy as np
v=np.asarray(csv_1)
print(v)
print(csv_1.sort_index(axis=0,ascending=False))
csv_1.loc[0,"Name"]="Riya"
print(csv_1)
print(csv_1.loc[[2,3],["Department","Salary"]])  # isme bs specific yhii data milega
print(csv_1.loc[:,["Department","Salary"]])  # isme bs yhii 2 column aayege sari row k
print(csv_1.loc[[2,3],:])  # isme row puri ayegi
print(csv_1.iloc[0,2])  # specific value deta h ye
print(csv_1.drop("Age",axis=1))  #ye age wala column drop ho jayega
print(csv_1.drop(1,axis=0))  # ye 1 wali row drop ho jayegi