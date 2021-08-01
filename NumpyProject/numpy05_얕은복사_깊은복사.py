import numpy as np

'''
  기본 파이썬의 얕은복사/깊은복사
    1. 깊은복사 3가지 구현
        copy(), [:], list()
        
    numpy는 [:]는 얕은 복사로 처리된다. (성능)
'''
#1. 기본 파이썬의 얕은복사
arr = list(range(10))
print("1. 원본:", arr)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = arr # 얕은복사
arr2[0] = 100
print("1.원본 수정됨:", arr)  # [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#2. 기본 파이썬의 깊은복사
arr = list(range(10))
print("1. 원본:", arr)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# copy_arr = arr.copy()
# copy_arr = arr[:]
copy_arr = list(arr)
copy_arr[0] = 100
print("1. 원본 수정안됨:",arr)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
####################################################################
####################################################################
####################################################################
arr = np.arange(10)
print("10. ndarray 원본:", arr)  # [0 1 2 3 4 5 6 7 8 9]

copy_arr = arr[:] # 얕은 복사로 동작된다.
copy_arr[0] = 100
print("10. ndarray 원본:", arr)  # [100   1   2   3   4   5   6   7   8   9]
#numpy 깊은 복사
arr = np.arange(10)
print("11. ndarray 원본:", arr)
# copy_arr = np.copy(arr)
copy_arr = arr.copy()
copy_arr[0] = 100
print("11. ndarray 원본(값변경 안됨):", arr)  # [0 1 2 3 4 5 6 7 8 9]

