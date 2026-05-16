import pandas as pd
var=pd.DataFrame({"Name":['a','b','c','d','a','c','b','d'],"s1":[20,40,25,45,10,20,15,12],"s2":[11,22,12,11,10,18,17,15]})
var1=var.groupby("Name")
print(var1)
for x,y in var1:
    print(x)
    print(y)
print(var1.get_group("a"))  
print(var1.min())
print(var1.max())
print(var1.mean())
print(var1.sum())
# list m convert krna
l=list(var1)
print(l)