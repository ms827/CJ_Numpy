import numpy as np

'''
  Numpy 함수 종류
  1. 일반 함수
  
  2. 유니버셜 함수 (universal function)
   ==> 데이터의 요소별로 연산을 수행하는 함수(벡터연산)
'''
#단항 유니버셜 함수

# 1. np.prod : 곱계산 (product)
arr = np.array([1,2,3,4])
print("1. np.prod(arr):", np.prod(arr)) # 24

arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print("1. np.prod(arr):", np.prod(arr)) # 720
print("1. np.prod(arr, keepdims=True):", np.prod(arr, keepdims=True)) # [[720]]
print("1. np.prod(arr, axis=0):", np.prod(arr, axis=0)) # [15 48]
print("1. np.prod(arr, axis=1):", np.prod(arr, axis=1)) # [ 2 12 30]

# 2. np.nanprod : nan값을 1로 처리

arr = np.array([[1,2],[3,4],[5, np.nan]]) # np.nan 이 null값 의미
print(arr)
'''
[[ 1.  2.]
 [ 3.  4.]
 [ 5. nan]]
'''
print("2. np.prod(arr)", np.prod(arr))  # nan
print("2. np.nanprod(arr)", np.nanprod(arr))  # 120.0
print("2. np.nanprod(arr, axis = 0)", np.nanprod(arr, axis = 0))  # [15.  8.]
print("2. np.nanprod(arr, axis = 1)", np.nanprod(arr, axis = 1))  # [ 2. 12.  5.]

# 3. np.cumprod : 누적 곱
arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print("3. np.cumprod(arr, axis = 0)", np.cumprod(arr, axis = 0))  # [[ 1  2] [1*3  2*4] [1*3*5 2*4*6]]
print("3. np.cumprod(arr, axis = 1)", np.cumprod(arr, axis = 1))  # [[ 1  1*2] [ 3 3*4] [ 5 5*6]]

# 1. np.prod : 곱계산 (product)
arr = np.array([1,2,3,4])
print("1. np.sum(arr):", np.sum(arr)) # 10

arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print("1. np.sum(arr):", np.sum(arr)) # 21
print("1. np.sum(arr, keepdims=True):", np.sum(arr, keepdims=True)) # [[21]]
print("1. np.sum(arr, axis=0):", np.sum(arr, axis=0)) # [9 12]
print("1. np.sum(arr, axis=1):", np.sum(arr, axis=1)) # [ 3 7 11]

# 2. np.nansum : nan값을 0으로 처리

arr = np.array([[1,2],[3,4],[5, np.nan]]) # np.nan 이 null값 의미
print(arr)
'''
[[ 1.  2.]
 [ 3.  4.]
 [ 5. nan]]
'''
print("2. np.nansum(arr)", np.nansum(arr))  # 15.0
print("2. np.nansum(arr, axis = 0)", np.nansum(arr, axis = 0))  # [9. 6.]
print("2. np.nansum(arr, axis = 1)", np.nansum(arr, axis = 1))  # [3. 7. 5.]


# 3. np.cumprod : 누적 합
arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print("3. np.cumsum(arr, axis = 0)", np.cumsum(arr, axis = 0))  # [[ 1  2] [1+3  2+4] [1+3+5 2+4+6]]
print("3. np.cumsum(arr, axis = 1)", np.cumsum(arr, axis = 1))  # [[ 1  1+2] [ 3 3+4] [ 5 5+6]]

#######################################################################################

# 4.np.mean : 평균
arr = np.array([1,2,3,4])
print("4. np.mean(arr):", np.mean(arr)) # 2.5

arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print("4. np.mean(arr, axis = 0)", np.mean(arr, axis = 0))  # [3. 4.]
print("4. np.mean(arr, axis = 1)", np.mean(arr, axis = 1))  # [1.5 3.5 5.5]


# 5. np.var : 분산
arr = np.array([1,2,3,4])
print("5. np.var(arr):", np.var(arr)) # 1.25
arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print("5. np.var(arr, axis = 0)", np.var(arr, axis = 0))  # [2.66666667 2.66666667]
print("5. np.var(arr, axis = 1)", np.var(arr, axis = 1))  # [0.25 0.25 0.25]

# 6. np.std : 표준편차 (분산 제곱근)
arr = np.array([1,2,3,4])
print("6. np.std(arr):", np.std(arr)) # 1.25
arr = np.array([[1,2],[3,4],[5,6]])
print(arr)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print("6. np.std(arr, axis = 0)", np.std(arr, axis = 0))  # [2.66666667 2.66666667]
print("6. np.std(arr, axis = 1)", np.std(arr, axis = 1))  # [0.25 0.25 0.25]

###############################################################

# 7. np.max(arr), np.min(arr)
arr = np.array([1,2,3,4])
print("1. np.max(arr):", np.max(arr)) # 4
print("1. np.max(arr):", np.min(arr)) # 1


arr = np.array([[11,2],[33,4],[5,62]])
print(arr)
'''
[[11  2]
 [33  4]
 [ 5 62]]
 '''
print("1. np.max(arr, axis = 0)", np.max(arr, axis = 0))  # [33 62]
print("1. np.max(arr, axis = 1)", np.max(arr, axis = 1))  # [11 33 62]
print("1. np.min(arr, axis = 0)", np.min(arr, axis = 0))  # [5 2]
print("1. np.min(arr, axis = 1)", np.min(arr, axis = 1))  # [2 4 5]


# 8. np.argmax, np.argmin ==> 인덱스 반환
arr = np.array([31,2,63,47])
print("2. np.argmax(arr):", np.argmax(arr)) # 2
print("2. np.argmin(arr):", np.argmin(arr)) # 1

arr = np.array([[11,2],[33,4],[5,62]])
print(arr)
'''
[[11  2]
 [33  4]
 [ 5 62]]
 '''
print("2. np.argmax(arr, axis = 0)", np.argmax(arr, axis = 0))  # [1 2]
print("2. np.argmax(arr, axis = 1)", np.argmax(arr, axis = 1))  # [0 0 1]
print("2. np.argmin(arr, axis = 0)", np.argmin(arr, axis = 0))  # [2 0]
print("2. np.argmin(arr, axis = 1)", np.argmin(arr, axis = 1))  # [1 1 0]

#####################################################################
# 9. np.sort : 정렬
arr = np.array([31,2,63,47])
print("3. np.sort(arr):", np.sort(arr))  # [ 2 31 47 63]
print("3. np.sort(arr):", np.sort(arr)[::-1])  # [ 2 31 47 63]

arr = np.array([[11,2,8,1,55,34],[33,4,100,2,5,88],[5,81,50,7,101,62]])
print(arr)
'''
[[ 11   2   8   1  55  34]
 [ 33   4 100   2   5  88]
 [  5  81  50   7 101  62]]

'''
print("3. np.sort(arr):", np.sort(arr))
'''
[[  1   2   8  11  34  55]
 [  2   4   5  33  88 100]
 [  5   7  50  62  81 101]]
'''
print("3. np.sort(arr, axis=None:", np.sort(arr, axis=None))
#  [  1   2   2   4   5   5   7   8  11  33  34  50  55  62  81  88 100 101]
print("3. np.sort(arr, axis=0:", np.sort(arr, axis=0))
'''
[[  5   2   8   1   5  34]
 [ 11   4  50   2  55  62]
 [ 33  81 100   7 101  88]]
'''
print("3. np.sort(arr, axis=1:", np.sort(arr, axis=1))
'''
[[  1   2   8  11  34  55]
 [  2   4   5  33  88 100]
 [  5   7  50  62  81 101]]
'''