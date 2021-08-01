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
arr = np.arange(16).reshape(4, 4)
print(arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

'''
c_split = np.vsplit(arr, 2)
print(c_split)
c1, c2 = np.vsplit(arr, 2)
print(c1, c2)

c, c2, c3, c4 = np.split(arr, 4, axis=0)
print(c1, c2, c3, c4)

