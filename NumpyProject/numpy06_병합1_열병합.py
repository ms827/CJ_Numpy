import numpy as np

'''
    병합(merge)
  1. 열병합
    - np.hstack
    - colum_stack
    - np.concatenate(   axis=1)
    
  2. 행병합
'''
arr = np.arange(9).reshape(3,3)
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
arr2 = arr * 2
print(arr2)
'''
[[ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''
c_merge = np.hstack((arr,arr2))
c_merge = np.column_stack((arr,arr2))
c_merge = np.concatenate((arr,arr2), axis=1)
print(c_merge)
'''
[[ 0  1  2  0  2  4]
 [ 3  4  5  6  8 10]
 [ 6  7  8 12 14 16]]
'''