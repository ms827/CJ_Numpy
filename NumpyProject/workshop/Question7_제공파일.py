# --------------------------------------------------------------------------
# 이 파일에서 제공되는 함수와 main() 수정하면 안되며
# 구현으로 표시된 함수를 응시생이 구현하여 프로그램을 완성해야 합니다.
# --------------------------------------------------------------------------

import numpy as np


# #제공 함수 수정 금지
def main():
    # 입력 : (n X m) 정수 리스트
    num = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # num = [[21, 42], [41, -5], [-7, 8], [60, 71], [4, 2], [5, 4]]

    #  (n X m) 정수 리스트를 ndarray 행렬로 변환하고 변환된 ndarray 행렬에서 짝수행(0, 2, 4, 6, ...)만 추출하는 함수 get_matrix() 호출
    #  get_matrix()함수 응시생 구현
    result_matrix = get_matrix(num)

    # 짝수행 행렬을 출력
    print_result(result_matrix)


# # 응시생 구현 함수
# (n X m) 정수 리스트를 ndarray 행렬로 변환하고 변환된 ndarray 행렬에서 짝수행(0, 2, 4, 6, ...)만 추출하는 기능
#
# @param		num		입력데이터( n X m 정수 리스트)
# @return				짝수행 행렬
def get_matrix(num):
    temp_matrix1 = None
    # 응시생 구현 시작
    return np.array(num)[::2]

    # 응시생 구현 끝
    return temp_matrix1


# #제공 함수 수정 금지
def print_line():
    print("-------------------------------------------------------------------------------")


# #제공 함수 수정 금지
def print_result(data):
    print_line()
    print("짝수행 추출 행렬: \n", data)
    print_line()


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
