import pandas as pd
#     MERGE
var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2=pd.DataFrame({"A":[1,2,3,5],"C":[21,22,23,24]})
print(pd.merge(var1,var2,on="A"))  # A jitna same hoga dono dataframe m utna data hi ayega
print(pd.merge(var1,var2,how="inner")) # ye bhii same wala data hi dega
print(pd.merge(var1,var2,how="left"))  # left means var1 wala data dega aurr var2 m jo data nhii h vo null ho jayega
print(pd.merge(var1,var2,how="right"))
print(pd.merge(var1,var2,how="outer"))  # ye full data show krega
print(pd.merge(var1,var2,how="outer",indicator=True)) # ye btayega ki konkonse data present h 

var3=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var4=pd.DataFrame({"A":[1,2,3,5],"B":[21,22,23,24]})  # jb dono m same ho
print(pd.merge(var3,var4,left_index=True,right_index=True,suffixes=("name","age")))

#     CONCAT
s1=pd.Series([1,2,3,4])
s2=pd.Series([11,22,33,44])
print(pd.concat([s1,s2]))

d1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
d2=pd.DataFrame({"A":[1,2,3,5],"B":[21,22,23,24]}) 
print(pd.concat([d1,d2])) 
print(pd.concat([d1,d2],axis=1,join="inner"))  # jo same hoga bs vhii ayega agar null value hogi to vo nhii ayega
print(pd.concat([d1,d2],keys=["d1","d2"]))  # axis=0 bydefault h
print(pd.concat([d1,d2],axis=1,keys=["d1","d2"])) 

d3=pd.DataFrame({"A":[1,2,3,4]})  
d4=pd.DataFrame({"B":[1,2,3,4],"C":[11,22,33,44]})
print(pd.concat([d3,d4]))  