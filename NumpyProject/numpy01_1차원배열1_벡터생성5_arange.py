import numpy as np

#파이썬의 range함수와 동일한 기능을 제공.
#np.arange(start, stop(필수), step, dtype) ==> 기본적으로 int 반환
v1 = np.arange(10)
print("1. np.arange(10): ", v1) #[0 1 2 3 4 5 6 7 8 9]

v1 = np.arange(1,5)
print("1. np.arange(1,5): ", v1) #[1 2 3 4]

v1 = np.arange(1,11,2)
print("1. np.arange(1,11,2): ", v1) #[1 3 5 7 9]

v1 = np.arange(10, dtype=float)
print("1. np.arange(10, dtype=float): ", v1) #[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

v1 = np.arange(10.0)
print("1. np.arange(10.0): ", v1) #[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]