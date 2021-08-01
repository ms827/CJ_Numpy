import numpy as np

'''
  Numpy 함수 종류
  1. 일반 함수

  2. 유니버셜 함수 ( universal function )
   ==> 데이터의 요소별로 연산을 수행하는 함수(벡터연산)

'''
# 이항 유니버셜 함수

# 1. np.add : + 기능
arr = np.array([1, 2, 3, 4])
arr2 = arr * 2
print(arr, arr2)  # [1 2 3 4] [2 4 6 8]
print("1. np.add(a,a2):", np.add(arr, arr2))  # [ 3  6  9 12]
print("1. arr+arr2:", (arr + arr2))  # [ 3  6  9 12]

# 2. np.subtract:  - 기능
arr = np.array([1, 2, 3, 4])
arr2 = arr * 2
print("2. np.subtract(a,a2):", np.subtract(arr, arr2))  # [-1 -2 -3 -4]
print("2. arr-arr2:", (arr - arr2))  # [ 3  6  9 12]

# 3. np.multiply:  * 기능
arr = np.array([1, 2, 3, 4])
arr2 = arr * 2
print("3. np.multiply(a,a2):", np.multiply(arr, arr2))  # [ 2  8 18 32]
print("3. arr*arr2:", (arr * arr2))  # [ 2  8 18 32]

# 4. np.divide:  / 기능
arr = np.array([1, 2, 3, 4])
arr2 = arr * 2
print("4. np.divide(a,a2):", np.divide(arr, arr2))  # [0.5 0.5 0.5 0.5]
print("4. arr/arr2:", (arr / arr2))  # [0.5 0.5 0.5 0.5]

# 5. np.floor_divide:  // 기능 ( 몫연산)
arr = np.array([1, 2, 3, 4])
arr2 = arr * 2
print("5. np.floor_divide(a,a2):", np.floor_divide(arr, arr2))  # [0 0 0 0]
print("5. arr//arr2:", (arr // arr2))  # [0 0 0 0]

# 6. np.mod:  % 기능 ( 나머지 연산)
arr = np.array([1, 2, 3, 4])
arr2 = arr * 2
print("6. np.mod(a,a2):", np.mod(arr, arr2))  # [1 2 3 4]
print("6. np.remainder(a,a2):", np.remainder(arr, arr2))  # [1 2 3 4]
print("6. arr%arr2:", (arr % arr2))  # [1 2 3 4]

# 7. np.maximum : 인덱스별 큰 값 반환
#  np.minimum,
arr = np.array([10, 2, 3, 4])
arr2 = np.array([1, 12, 3, 14])
print("7. np.maximum(a,a2):", np.maximum(arr, arr2))  # [10 12  3 14]
print("7. np.minimum(a,a2):", np.minimum(arr, arr2))  # [1 2 3 4]

# 8. np.greater : 인덱스별 비교해서 boolean 값 반환
# greater_equal
arr = np.array([10, 2, 3, 4])
arr2 = np.array([1, 12, 3, 14])
print("8. np.greater(a,a2):", np.greater(arr, arr2))  # [ True False False False]
print("8. arr > arr2:", (arr > arr2))  # [ True False False False]
print("8. np.greater_equal(a,a2):", np.greater_equal(arr, arr2))  # [ True False  True False]
print("8. arr >= arr2:", (arr >= arr2))  # [ True False  True False]
print("8. np.less(a,a2):", np.less(arr, arr2))  # [False  True False  True]
print("8. np.less_equal(a,a2):", np.less_equal(arr, arr2))  # [False  True  True  True]
print("8. np.equal(a,a2):", np.equal(arr, arr2))  # [False False  True False]
print("8. np.not_equal(a,a2):", np.not_equal(arr, arr2))  # [ True  True False  True]

# 9. np.power : 제곱   ,  np.sqrt : 제곱근
print("9.  np.power(3,2)", np.power(3, 2))  # 9
print("9.  np.power([3,2,4],2)", np.power([3, 2, 4], 2))  # [ 9  4 16]
print("9.  np.power([3,2,4],[4,2,5])", np.power([3, 2, 4], [4, 2, 5]))  # [  81    4 1024]

print(np.greater)  # <ufunc 'greater'>