import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
a=arr.flatten()
a[0]=10
print(arr)
print(a)
b=arr.ravel()
b[0]=20
print(arr)
print(b)