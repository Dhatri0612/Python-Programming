import pandas as pd
v1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]},index=['a','b','c','d'])
v2=pd.DataFrame({"C":[10,20],"B":[21,22]},index=['a','b'])
print(v1.join(v2,how="outer",lsuffix="_14",rsuffix="_12"))
