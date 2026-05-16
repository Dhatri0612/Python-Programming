import pandas as pd
var_1=ar=pd.read_csv("C:\\Users\\USER\\OneDrive\Desktop\\test_missingData.csv")
# print(var_1.fillna("Python"))
# print(var_1.fillna({"Name":"Ruhi","Age":25,"Salary":40000}))
# var_1.fillna(method="ffill")  ye error de rhaa h
#print(var_1.ffill())  # forward filling h ye isme just phle row wala data jo full null wali row m aajata h
#print(var_1.bfill())  # backword filling h ye isme just baad wali row ka data jo full null row hoti h usme aajata h
#print(var_1.ffill(axis=1))  # ye aese axis k along fill krta h aurr axis=0 by default hota h
#print(var_1.fillna({"Name":"Unknown", "Age":12,"Department":"No Dept", "Salary":12000},inplace=True))  # null ki jghh ye value fill kr dete h
print(var_1.fillna("Python",limit=1)) # jo phle null ayega vhaa ye fill krdega
