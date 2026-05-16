import pandas as pd
var=pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]})
print(var)
# insert 
var.insert(1,"p",var["a"])
print(var)
var.insert(2,"p_1",[11,12,13,14]) # no of data phle wale data k equal hona chahiye
print(var)

# data ko copy krwana h perticular point tk
var["python"]=var["a"][:3]
print(var)

# delete
v=pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8],"c":[11,22,33,44]})
print(v)
v.pop("b")
print(v)
del v["a"]
print(v)