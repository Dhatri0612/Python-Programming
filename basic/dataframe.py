import pandas as pd
l=[1,2,3,4,5,6,7,8]
var=pd.DataFrame(l)
print(var)
print(type(var))

d={"a":[1,2,3,4],"s":[1,2,3,4],"c":[1,2,3,4],1:[1,2,3,4]}
var1=pd.DataFrame(d)
print(var1)
print(type(var1))
print(var1["a"][2])

l1=[[1,2,3,4,5],[6,7,8,9,10]]
var2=pd.DataFrame(l1)
print(var2)

sr={"s":pd.Series([1,2,3,4,5]),"r":pd.Series([1,2,3,4,5])}
var3=pd.DataFrame(sr)
print(var3)
print(type(var3))