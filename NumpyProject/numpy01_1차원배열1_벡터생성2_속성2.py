import numpy as np

list_value = [10,20,30]
v1=np.array(list_value)
print("1. 벡터의 차원(dimension):", v1.ndim) # 1 (차원)
print("2. 벡터의 차원 크기(튜플):", v1.shape) # (3,)
print("3. 벡터의 총 요소 개수:", v1.size) # 3
print("4. 벡터의 총 요소 타입:", v1.dtype) # int32 ==> 4byte (1byte=8bit)
