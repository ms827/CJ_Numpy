import numpy as np

'''
    1. 1차원 ==> 2차원 변경
        1) shape = (행,열)
        2) reshape(행,열) 함수
        
    2. 2차원 ==> 1차원 변경
        1) flatten()
            
        
        2) ravel()
'''

list_value = [[10,20,30],[1,2,3],[4,5,6]]
arr1 = np.array(list_value)
print(arr1)
'''
[[10 20 30]
 [ 1  2  3]
 [ 4  5  6]]
 '''
print("1. flatten() 행단위:",arr1.flatten()) #[10 20 30  1  2  3  4  5  6]
print("2. ravel() 행단위:",arr1.ravel()) #[10 20 30  1  2  3  4  5  6]

print("3. flatten(order='F') 열단위:",arr1.flatten(order='F')) #[10  1  4 20  2  5 30  3  6]
print("3. ravel(order='F') 열단위:",arr1.ravel(order='F')) #[10  1  4 20  2  5 30  3  6]

#내부적인 동작 방식이 다르다.
list_value = [[1,2,3],[4,5,6]]
arr1 = np.array(list_value)
print(arr1)
'''
[[1 2 3]
 [4 5 6]]
'''
x1 = arr1.flatten()
x2 = arr1.ravel()
print("-----------------2차원 배열 수정전-----------------")
print("1. flatten:", x1) #[1 2 3 4 5 6]
print("1. ravel:", x2) #[1 2 3 4 5 6]
print("-----------------2차원 배열 수정후-----------------")
arr1[0][0]=100
print(arr1) # [100   2   3   4   5   6]
print("1. flatten:", x1) #[1 2 3 4 5 6] ==> 깊은복사가 되서 원본 값 변경이 안된다
print("1. ravel:", x2) #[100   2   3   4   5   6] ==> 얕은 복사가 되서 원복 값이 변경된다