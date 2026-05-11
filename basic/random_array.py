import numpy as np
# rand
arr=np.random.rand(2,3)
print(arr)
# randn
arr = np.random.randn(2,3)
print(arr)
# randint
arr1=np.random.randint(1,101,10)
print(arr1)
# shape
arr2=np.random.rand(3,3)
print("Shape :",arr2.shape)
# random value pick
array=np.random.choice([10,20,30,40],size=5)
print(array)
# same random output
np.random.seed(22)
arr3=np.random.rand(2,2)
print(arr3)