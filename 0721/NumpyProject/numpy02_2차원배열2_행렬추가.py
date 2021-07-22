import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
'''
[[1 2 3]
 [4 5 6]]

'''
'''
  2차원 배열 추가/삽입
    1. np.append 함수이용
    2. axis지정하지 않으면 1차원 반환
    따라서 기존배열의 열 개수와 일치하지 않아도 된다.
    3.axis 지정하면 반드시 기존배열의 열 및 행 개수와 일치해야 한다 : dimension이 반드시 일치해야한다
'''

# 1. 추가 : np.append(arr,값) axis 지정하지 않으면 자동으로 flatten 된다
arr_copy = np.append(arr, [[9,8,7,3,2,5,6]])
print(arr_copy)  # [1 2 3 4 5 6 9 8 7 3 2 5 6]

arr_copy = np.append(arr, [[9,8,7]], axis=0)
print(arr_copy)
'''
[[1 2 3]
 [4 5 6]
 [9 8 7]]
'''

'''
실습
[[1 2 3 100]
[4 5 6 200]]
'''

arr = np.array([[1,2,3],[4,5,6]])
copy_arr = np.append(arr, [[100],[200]], axis=1)
print(copy_arr)

# 2. 삽입: np.insert(arr, idx, axis)
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
'''
[[1 2 3]
 [4 5 6]]
'''
arr_copy = np.insert(arr,0,200) # [200   1   2   3   4   5   6]
print(arr_copy)

arr_copy = np.insert(arr,0,100,axis=1)
print(arr_copy)
'''
[[100   1   2   3]
 [100   4   5   6]]
'''
arr_copy = np.insert(arr,0,100,axis=0)  #브로드캐스팅
print(arr_copy)
'''
[[100 100 100]
 [  1   2   3]
 [  4   5   6]]
'''
arr = np.arange(5)
print(arr)
'''
[0 1 2 3 4] * 4 ==> [0 1 2 3 4] * [4 4 4 4 4]  브로드캐스팅
'''