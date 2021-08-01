import numpy as np

# 1. 2차원 배열인 행렬 생성 - 중첩리스트
list_value = [[10,20,30],[1,2,3]]
arr1 = np.array(list_value)
print(arr1, type(arr1)) # <class 'numpy.ndarray'>

# 2. 1차원 --> 2차원 변경, shape 속성 이용
list_value = [1,2,3,4,5,6]
arr1 = np.array(list_value)
print(arr1) # [1 2 3 4 5 6]
arr1.shape=(1,6) #1행6열
print(arr1) # [[1 2 3 4 5 6]]
arr1.shape=(6,1) #6행1열
print(arr1) # [[1][2][3][4][5][6]]
arr1.shape=(2,3) #2행3열
print(arr1) # [[1 2 3] [4 5 6]]
arr1.shape=(3,2) #3열2행
print(arr1) # [[1 2] [3 4] [5 6]]

#행과 열중에서 하나만 지정하고 나머지는 -1 지정하면, 자동으로 계산을 해서 -1값 대신에 치환된다.
arr1.shape=(3,-1)
print(arr1)

