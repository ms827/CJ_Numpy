import numpy as np

v1 = np.array([9,8,7,6,5])

# 1. 추가 ==> np.append()
v1_copy = np.append(v1, 100)
print(v1) # [9 8 7 6 5]
print(v1_copy) # [  9   8   7   6   5 100]

# 2. 삽입 ==> np.insert
v1_copy = np.insert(v1, 0, 100)
print(v1_copy) # [100   9   8   7   6   5]

# numpy에서 색인은 여러개 지정 가능 : [idx1,idx2] ==> fancy 색인이라고 부른다
v1_copy = np.insert(v1, [0,2],100)
print(v1_copy) # [100   9   8 100   7   6   5]
v1_copy = np.insert(v1, [1,2,3],100)
print(v1_copy) # [  9 100   8 100   7 100   6   5]
# v1_copy = np.insert(v1, slice(1,4),100)
# print(v1_copy) # [  9 100   8 100   7 100   6   5]