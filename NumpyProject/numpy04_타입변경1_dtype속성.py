import numpy as np

'''
  ndarray의 데이터 타입 변경
  
  1. dtype 속성으로 변경
  
  2. astype 함수로 변경
'''

# 1. int --> float
arr = np.array([10,20,30])
print(arr, type(arr), arr.dtype) # [10 20 30] <class 'numpy.ndarray'> int32

f_arr = np.array([10,20,30], dtype=float)
print(f_arr, f_arr.dtype)

f_arr = np.array([10,20,30], dtype='f8')
print(f_arr, f_arr.dtype)

# 2. float --> int
arr = np.array([10.,20,30])
print(arr, type(arr), arr.dtype) #<class 'numpy.ndarray'> float64

i_arr = np.array([10.,20,30], dtype=int)  #[10 20 30] int32
i_arr = np.array([10.,20,30], dtype="i8")  #[10 20 30] int64
print(i_arr, i_arr.dtype)

# 4. int --> bytes, str
arr = np.array([10,20,30])
print(arr, type(arr), arr.dtype)

s_arr = np.array([10,20,30], dtype=str)
print(s_arr, s_arr.dtype)  # ['10' '20' '30'] <U2

s_arr = np.array([10,20,30], dtype=bytes)  # dtype=np.string_
print(s_arr, s_arr.dtype)  # [b'10' b'20' b'30'] |S2

# 4. str --> int

arr = np.array(['10','20'])
print(arr, arr.dtype)  # ['10' '20'] <U2
i_arr = np.array(['10','20'], dtype=int)
print(i_arr, i_arr.dtype) # [10 20] int32