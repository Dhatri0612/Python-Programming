import numpy as np

arr=np.array([10,20,30,40])
# indexing
print(arr[0])
#  attributes
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
# slicing
print(arr[1:4])
# boolean indexing
print(arr[arr>20])

# 2D Array
arr1=np.array([[1,2,3,4],
              [5,6,7,8]])
# indexing
print(arr1[1,1])
