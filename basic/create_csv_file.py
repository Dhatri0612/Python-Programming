import pandas as pd
d=pd.DataFrame({"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5]})
print(d)
d.to_csv("Test_new",index=False,header=["i","j","k"])