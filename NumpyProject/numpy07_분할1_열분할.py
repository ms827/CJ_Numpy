import numpy as np

'''
    분할(split)
    
  1. 열분할
    - np.hsplit
    - np.column_split
    - np.split(   axis=1)
    
  2. 행분할
    - np.vsplit
    - np.row_split
    - np.split(   axis=0)
'''
arr = np.arange(12).reshape(3, 4)
print(arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

'''
c_split = np.hsplit(arr, 2)
print(c_split)
c1, c2 = np.hsplit(arr, 2)
print(c1, c2)

c, c2, c3, c4 = np.split(arr, 4, axis=1)
print(c1, c2, c3, c4)

