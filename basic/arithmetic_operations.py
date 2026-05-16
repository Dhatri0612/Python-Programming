import pandas as pd
var=pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]})
print(var)
var["c"]=var["a"]+var["b"] # +-*/ sb aese hi hote h
print(var)

var1=pd.DataFrame({"a":[10,20,30,40],"b":[15,16,17,18]})
print(var1)
var1["python"]=var1["a"]<=20
var1["python_1"]=var1["b"]>=16
print(var1)
