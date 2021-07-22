import numpy as np


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print("1. arr[0] \n",arr[0]) #  [1 2 3]
print("2. arr[행, 열] \n",arr[0, 1]) # 0행1열,  2
print("3. arr[행, 슬라이싱] \n",arr[0, 1:]) #  [2 3]
print("4. arr[행, fancy 색인] \n",arr[0, [0,2]]) #  [1 3]

print("5. arr[슬라이싱, 열] \n",arr[1:,1]) #   [5 8]
print("6. arr[fancy 색인, 열] \n",arr[[0,2],1]) #   [2 8]

print("7. arr[슬라이싱,슬라이싱] \n",arr[1:, :2]) #  [[4 5]  [7 8]]
print("8. arr[fancy 색인,fancy 색인] \n",arr[[0,2], [0,2]]) #   [1 9]


