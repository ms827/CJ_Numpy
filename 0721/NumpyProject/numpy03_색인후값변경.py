import numpy as np

'''
  색인(인덱싱, 슬라이싱, fancy, boolean) 후 값 변경
'''

arr = np.arange(10)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
arr[0] = 100
print(arr)  # [100   1   2   3   4   5   6   7   8   9]
####################################
# arr[슬라이싱] = 값
arr[:4]=200
print(arr)

# arr[fancy색인] = 값
arr[[0,5]] = 300
print(arr)

# arr[boolean색인] = 값
arr[arr < 100] = 999
print(arr)