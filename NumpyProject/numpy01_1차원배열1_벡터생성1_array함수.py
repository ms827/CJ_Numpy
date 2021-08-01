import numpy as np

# 1.numpy 버전 확인
print("1. numpy 버전 확인:",np.__version__) #1.21.1

# 2. 1차원 배열인 벡터 생성
list_value = [10,20,30]
vector01=np.array(list_value)
print(vector01, type(vector01)) # [10 20 30] <class 'numpy.ndarray'>

list_value2 = [x for x in range(10)]
vector02 = np.array(list_value2)
vector02 = np.array([x for x in range(10)])
print(vector02)

# 3. 자동 형변화 => numpy의 모든 데이터는 통일된다.(형변환)
int_float_value = [1,2,3, 4.]
print(int_float_value) # [1, 2, 3, 4.0]
vector03 = np.array(int_float_value)
print(vector03) #[1. 2. 3. 4.]