import numpy as np
a=np.array([1,2,3,4])
b=5
print(a+b)

b = np.array([[1,2,3],
              [4,5,6]])
c = np.array([10,20,30])
print(b+c)

d = np.array([[1],
              [2],
              [3]])
e=np.array([10,20,30])
print(d+e)

# f = np.array([1,2,3])
# g = np.array([1,2])
# print(f+g)  #Error

arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
a1=np.array([1,2,3])
print(arr+a1)