import numpy as np

r1 = np.random.random() #[0.0, 1.0) ==> 0.0 <= 값 <1.0
print("1. random(): ",r1)

r2 = np.random.random(5) # 랜덤값 5개 반환
print("2. random(5): ", r2) #[0.97592644 0.92843398 0.73438223 0.57887867 0.57760853]

r3 = np.random.rand(5) # 0~1 사이의 균등분포에서 랜덤값 추출
print("3. rand(5): ", r3) #

r4 = np.random.randn(5) # 평균값이 0이고 표준편차가 1인 정규분포에서 랜덤값 추출
print("4. randn(5): ", r4)

r5 = np.random.randint(1,11) # 1~10 까지의 랜덤값
print("5. randint(1,11): ", r5)

r5 = np.random.randint(low=1,high=11,size=3, dtype=np.int64) # 1~10 까지의 랜덤값, 중복추출
print("5. randint(1,11,3): ", r5)

# 0~6 까지 3개 추출
r5 = np.random.randint(7, size=3) # 0~6,3개 추출 low=0 일경우 생략가능
print("5. randint(7, size=3): ", r5)

##################################################
r6= np.random.choice(["A","B","C"])
print("6. choice(): ", r6)

list_value=[6,5,8,5,4,11,79]
np.random.shuffle(list_value)
print("7. shuffle(): ",list_value)