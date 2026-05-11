import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr.shape)
a=arr.reshape(2,3)
print(a)

arr1=np.array([1,2,3,4,5,6,7,8])
print(arr1)
print(arr1.reshape(4,2))
print(arr1.reshape(2,2,2))

arr2=np.arange(1,13)
print(arr2)
print(arr2.reshape(3,4))
print(arr2.T)

print(arr.reshape(2,-1))
print(arr.reshape(-1,3))