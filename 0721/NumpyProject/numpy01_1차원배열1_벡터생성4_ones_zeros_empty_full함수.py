import numpy as np

# ones
r1 = np.ones(5)
print("1. ones(5): " , r1, r1.dtype) # [1. 1. 1. 1. 1.] float64

r1 = np.ones(5, dtype=int)  # deprecated: 과거에는 사용했지만 현재는 사용을 권장하지 않음 의미.
print("1. ones(5): " , r1, r1.dtype)

# zeros
r1 = np.zeros(5)
print("2. zeros(5): " , r1, r1.dtype) # [0. 0. 0. 0. 0.] float64

r1 = np.zeros(5, dtype=int)
print("2. zeros(5): " , r1, r1.dtype) # [0 0 0 0 0] int32

# empty ==> 임의의 값으로 채움. 즉, 초기화할 의도가 있음
r1 = np.empty(5, dtype=int)
print("3. empty(5): " , r1, r1.dtype)

# full(크기, 값, dtype)
r1 = np.full(5, 10)
print("4. full(5, 10): " , r1, r1.dtype) # [10 10 10 10 10] int32