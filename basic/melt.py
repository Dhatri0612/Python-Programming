import pandas as pd
var=pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[15,16,17,18,12,15],"maths":[11,12,14,15,17,18]})
print(var)
print(pd.melt(var,id_vars=["days"],var_name="python",value_name="number"))