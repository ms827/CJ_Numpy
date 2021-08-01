import numpy as np

'''
  Numpy 함수 종류
  1. 일반 함수
  
  2. 유니버셜 함수 (universal function)
   ==> 데이터의 요소별로 연산을 수행하는 함수(벡터연산)
'''
#단항 유니버셜 함수

#1. np.abs : 절대값, np.absolute 동일
arr = np.array([4.56, -2.19, 0 ,1.57, 3.440, -89.46])
print("1. np.abs(arr)", np.abs(arr))
print("1. np.abs(arr)", np.absolute(arr))

#2. np.around : 0.5 기준으로 올림 또는 내림 ==> 실행결과는 정수형으로 반환
arr = np.array([4.56, -2.19, 0 ,1.57, 3.440, -89.46])
print("2. np.around(arr)",np.around(arr))

#3. np.round : 소수점 n자리 반올림
arr = np.array([4.51546, -2.194568, 0 ,1.53457, 3.401840, -89.469754])
print("3. np.round(arr,1)",np.round(arr)) # [  5.  -2.   0.   2.   3. -89.]
print("3. np.round(arr,1)",np.round(arr, 1)) # [  4.5  -2.2   0.    1.5   3.4 -89.5]
print("3. np.round(arr,1)",np.round(arr, 2)) # [  4.52  -2.19   0.     1.53   3.4  -89.47]

#4, np.rint : 가장 가까운 정수로 올림 또는 내림
arr = np.array([4.56, -2.19, 0 ,1.57, 3.440, -89.46])
print("4, np.rint(arr)", np.rint(arr)) # [  5.  -2.   0.   2.   3. -89.]

#5. np.ceil : 같거나 큰수중 가장 작은 정수값으로 올림
arr = np.array([4.56, -2.19, 0 ,1.57, 3.440, -89.46])
print("5, np.ceil(arr)", np.ceil(arr)) # [  5.  -2.   0.   2.   3. -89.]

#6. np.floor : 같거나 작은수중 가장 큰 정수값으로 내림
arr = np.array([4.56, -2.19, 0 ,1.57, 3.440, -89.46])
print("6, np.floor(arr)", np.floor(arr)) # [  4.  -3.   0.   1.   3. -90.]

#7. np.trunc : 소수점 버리고 정수로 반환
arr = np.array([4.56, -2.19, 0 ,1.57, 3.440, -89.46])
print("7, np.trunc(arr)", np.trunc(arr)) # [  4.  -2.   0.   1.   3. -89.]

#8. np.sqrt : 제곱급
arr = np.array([1,4,9,16])
print("8, np.sqrt(arr)", np.sqrt(arr)) # [1. 2. 3. 4.]
