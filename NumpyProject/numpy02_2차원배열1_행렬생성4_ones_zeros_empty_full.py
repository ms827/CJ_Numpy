import numpy as np

#zeros
arr = np.zeros((2,3))
print(arr)
arr = np.zeros((2,3), dtype=int)
print(arr)

#ones
arr = np.ones((2,3))
print(arr)
arr = np.ones((2,3), dtype=int)
print(arr)

#empty
arr = np.empty((4,5))
print(arr)

#full(tuple,값)
arr = np.full((2,3), 100)
print(arr)

#단위행렬
kkk = np.eye(3)
print(kkk)