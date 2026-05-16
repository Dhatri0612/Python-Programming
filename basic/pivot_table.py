import pandas as pd
var=pd.DataFrame({"days":[1,1,1,1,2,2],"s_name":['a','b','a','a','b','b'],"eng":[15,16,17,18,12,15],"maths":[11,12,14,15,17,18]})
# print(var.pivot(index="days",columns="s_name",values="eng"))
print(var.pivot_table(index="s_name",columns="days",aggfunc="sum"))