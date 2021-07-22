import numpy as np

# 1. 2차원 배열인 행렬 생성 - 중첩튜플
list_value = [[10,20,30],[1,2,3]]
arr1 = np.array(list_value)
print("1. 2차원 배열의 차원(dimension):", arr1.ndim) # 2 (차원)
print("2. 2차원 배열의 차원 크기(튜플):", arr1.shape) # (2, 3)
print("3. 2차원 배열의 총 요소 개수:", arr1.size) # 6
print("4. 2차원 배열의 대이터 타입:", arr1.dtype) # int32 ==> 4byte (1byte=8bit)

'''
  int8:  1byte  : -128 ~ 127
  int16: 2byte  : -32768 ~ 32767
  int32: 4byte  : -2147483648 ~ 2147483647  (기본)
  int64: 8byte  : 
'''