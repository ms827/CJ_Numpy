import numpy as np

'''
   ndarray의 데이터 타입 변경

   1.  dtype 속성으로 변경

   2. astype 함수로 변경

'''

# 1. int --> float
arr = np.array([10, 20, 30])
print(arr, type(arr), arr.dtype)  # [10 20 30] <class 'numpy.ndarray'> int32
arr = arr.astype(float)
print(arr, type(arr), arr.dtype)  # [10. 20. 30.] <class 'numpy.ndarray'> float64

# 2. float --> int
arr = np.array([10., 20, 30])
print(arr, type(arr), arr.dtype)  # [10. 20. 30.] <class 'numpy.ndarray'> float64
arr = arr.astype(int)
print(arr, type(arr), arr.dtype)  # [10 20 30] <class 'numpy.ndarray'> int32

# 3. int --> bytes, str
arr = np.array([10, 20, 30])
print(arr, type(arr), arr.dtype)
# arr = arr.astype(str)
arr = arr.astype(bytes)
print(arr, type(arr), arr.dtype)  # ['10' '20' '30'] <class 'numpy.ndarray'> <U11
# 4. str --> int
arr = np.array(['10', '20'])
print(arr, arr.dtype)
arr = arr.astype(int)
print(arr, arr.dtype)  # [10 20] int32