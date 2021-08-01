import numpy as np


'''
  2차원 배열 추가/삽입
    1. np.delete 함수이용
    2. axis지정하지 않으면 1차원 반환
    따라서 기존배열의 열 개수와 일치하지 않아도 된다.
    3.axis 지정하면 반드시 기존배열의 열 및 행 개수와 일치해야 한다 : dimension이 반드시 일치해야한다
'''
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
'''
[[1 2 3]
 [4 5 6]]
'''

copy_arr = np.delete(arr, 3) # axis지정하지 않으면 flatten된다
print(copy_arr) #[1 2 3 5 6]

copy_arr = np.delete(arr, 0, axis=1) # axis지정하지 않으면 flatten된다
print(copy_arr)
'''
[[2 3]
 [5 6]]
 '''
copy_arr = np.delete(arr, 0, axis=0) # axis지정하지 않으면 flatten된다
print(copy_arr) #[[4 5 6]]
