import numpy as np

v1 = np.array([9,8,7,6,5])
# 1. 삭제 ==> np.delete(arr, idx, axis=0)
v1_copy = np.delete(v1, 0) # [8 7 6 5]
print(v1_copy)

#fancy 색인 사용 가능
v1_copy = np.delete(v1, [0,1,2]) # [6 5]
print(v1_copy)

# 2. 값으로 삭제
v1 = np.array([9,8,7,6,5])
print(np.where(v1==5))
v1_copy = np.delete(v1, np.where(v1==5)) #[9 8 7 6]
print(v1_copy)
