import numpy as np


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
#1.boolean 색인
print("1. 벡터연산: ", arr%2==0)
print("2. 짝수값 출력: ", arr[arr%2==0]) # [2 4 6 8]
print("3. 짝수값이면서 5보다 작은값 출력: ", arr[(arr%2==0) & (arr <5)]) # [2 4]
print("3. 짝수값이거나 5보다 작은값 출력: ", arr[(arr%2==0) | (arr <5)]) # [1 2 3 4 6 8]
print("3. 홀수값이거나 5보다 작은값 출력: ", arr[~(arr%2==0) | (arr <5)]) # [1 2 3 4 5 7 9]
