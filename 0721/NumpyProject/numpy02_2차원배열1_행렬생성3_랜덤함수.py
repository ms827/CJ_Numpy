import numpy as np

np.random.seed(1234) # 랜덤값 고정
arr = np.random.random((2,3)) # 2행 3열 랜덤값
print(arr)

arr = np.random.rand(2,3)
print(arr)

arr = np.random.randn(2,3)
print(arr)

arr = np.random.randint(7,size=(2,3))
print(arr)