import pandas as pd
var=pd.read_csv("C:\\Users\\USER\\OneDrive\\Desktop\\test.csv")
print(var.replace(to_replace="Person_1",value="Person_New"))
print(var.replace([1,2,3,4,5,6,7,8],22))  # list
# print(var.replace("[A-Za-z]","p",regex=True))  # regex
print(var.replace({"Name":"[A-Z]"},"ho",regex=True))
# print(var.replace(2,method="ffill"))  # ye is python verson m work nhii kr rhaa h 
print(var.replace(2,pd.NA).ffill())  # new verson m ye chalega
print(var.replace(2,pd.NA).ffill(limit=2))  #ye limit lgaa deta h
print(var.replace(2,pd.NA).ffill(limit=2,inplace=True))  # ye original data m change hota h koii copy nhii bnata h
 