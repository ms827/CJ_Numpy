import numpy as np

# 1. np.nonzero() ==> 0이 아닌 값의 index 반환
arr = np.array([3,55,0,8,0,131])
print("1. np.nonzero :", np.nonzero(arr))  # (array([0, 1, 3, 5], dtype=int32),)

# 2. np.where : 3항연산자 (기억할것)
arr = np.arange(10)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
# 3항 연산자: 참 if 조건식 else 거짓
print("2. np.where :", np.where(arr<5, arr, arr*10))  # [ 0  1  2  3  4 50 60 70 80 90]

# 3.np.where : 값의 위치값 반환
arr = np.array([9,3,6,87])
print("3. np.where :", np.where(arr == 3))  # np.where : (array([1], dtype=int64),)
arr = np.array([[9,3,6],[3,66,5]])
print("3. np.where :", np.where(arr == 3))  # (array([0, 1], dtype=int32), array([1, 0], dtype=int64))

############################################################

#4. np.unique : 중복값 제거후 정렬해서 반환
arr = np.array([9,3,6,87,9,4,45,1])
print("4. np.unique :", np.unique(arr))  # [ 1  3  4  6  9 45 87]

arr = np.array([[9,3,54,7],[7,3,5,67]])
print("4. np.unique :", np.unique(arr))  # [ 3  5  7  9 54 67]
############################################################
# 5. np.choose : fancy색인 동일

arr = np.array(["A","B","C","D","E"])
print("5. A와B와E 색인 :", arr[[0,1,4]])  # ['A' 'B' 'E']
print("5. A와B와E 색인 :", np.choose([0,1,4],arr))  # ['A' 'B' 'E']

############################################################
# 6. np.select : 다중 조건 지정
x = np.arange(10)
print(x)  # [0 1 2 3 4 5 6 7 8 9]
condlist = [x<3, x>5]
choicelist = [x, x**2]
print("6. np.select :", np.select(condlist, choicelist))  # [ 0  1  2  0  0  0 36 49 64 81]
print("6. np.select :", np.select(condlist, choicelist, default=-1))  # [ 0  1  2 -1 -1 -1 36 49 64 81]
############################################################
# 7. np.all, np.any ==> boolean 값을 이용
print("7. np.all:", np.all([True,True]))  # True
print("7. np.all:", np.all([True,True,False]))  # False
print("7. np.any:", np.any([True,True]))  # True
print("7. np.any:", np.any([True,True,False]))  # True
print("7. np.any:", np.any([False,False]))  # False
# 응용
arr = np.array(["HI", "he","His"])
print("모든 문자가 대문자? ", np.char.isupper(arr))
print("모든 문자가 대문자? ", np.all(np.char.isupper(arr)))

print("대문자가 있어? ", np.char.isupper(arr))
print("대문자가 있어? ", np.any(np.char.isupper(arr)))

print("모든 길이가 3보다 길어?", np.all([len(x) >= 3 for x in arr]))
print("모든 길이가 3보다 길어?", np.all(np.char.str_len(arr)>=3))

############################################################
# 8. np.fromstring ==> split 기능포함
result = np.fromstring('10 20', sep=" ")
print(result, result.dtype)  # [10. 20.] float64
result = np.fromstring('10 20', sep=" ", dtype = int)
print(result, result.dtype)  # [10. 20.] int32

# 응용
# '10 20 30' => 합계산?
xxx = np.sum(np.fromstring('10 20 30', sep=" ", dtype=int))
print(xxx)

############################################################
# 9. 전치 ( transpose )
arr = np.arange(15).reshape(3,5)
print(arr)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''
print("전치: ", arr.T)
print("전치: ", np.transpose(arr))

#####################################################################################
# 10. 내적 (  np.dot()
arr = np.arange(4).reshape(2,2)
print(arr)
print("내적: ",  np.dot(arr, arr))