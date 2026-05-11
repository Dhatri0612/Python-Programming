import numpy as np
#  1D
arr=np.array([10,20,30,40,50])
print("First element: ",arr[0])
print("Last element: ",arr[-1])
print(arr[1:4])
print(arr[::-1])

# 2D
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1[1,1])
print(arr1[2,2])
print(arr1[1])
print(arr1[2])

print(arr1[0:2,0:2])
print(arr1[-2:]) # last two row
print(arr1[:,0]) # hr row ka first element
print(arr[arr>20])