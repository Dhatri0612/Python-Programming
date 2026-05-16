import pandas as pd
x=[1,2,3,4,5]
var=pd.Series(x,index=['a','b','c','d','e'],dtype="float",name="python")
print(var)
print(type(var))

y={"name":["python","C","Java","SQL"], "por":[12,14,15,17],"rank":[1,2,4,3]}
var1=pd.Series(y)
print(var1)

s=pd.Series(12,index=[1,2,3,4,5,6,7,8])
print(s)

a1=pd.Series(12,index=[1,2,3,4,5,6,7])
a2=pd.Series(12,index=[1,2,3,4])
print(a1+a2)