import pandas as pd
var=pd.read_csv("C:\\Users\\USER\\OneDrive\Desktop\\test_missingData.csv")
print(var.dropna()) # isse NaN wali sari row hatt jayegi
print(var.dropna(axis=0))  # NaN wali row hatt jayegi
print(var.dropna(axis=1))  # NaN wale column hatt jayege
print(var.dropna(how="any"))  # NaN jiss jiss row m thaa vo puri row ht gyyi
print(var.dropna(how="all"))  # jiss bhii puri row m sari value NaN hogi vo row hatt jayegi
print(var.dropna(subset=["Salary"]))  # is column m jo bhii null value hogi vo hatt jayegi
var.dropna(inplace=True)  #
print(var)
var.dropna(thresh=1)  # jiss row k andar 1 null value hogi vo row hatt jayegi
print(var)
