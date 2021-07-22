import numpy as np

#linspace(start, stop, num, endpoint= True) : 특정 범위에서 균일한 간격으로 값을 num개 생성
v1 = np.linspace(0,1,11) # 0 ~ 1 범위에서 11개 값을 반환
print(v1)

v1 = np.linspace(0,0.9,10) # 0 ~ 0.9 범위에서 10개 값을 반환
print(v1)

v1 = np.linspace(0,0.9,10,endpoint=True) # endPoint=True는 stop포함
print(v1)

v1 = np.linspace(0,0.9,10,endpoint=False) # endPoint=False는 stop미포함
print(v1)