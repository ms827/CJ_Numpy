import numpy as np

# arange + reshape(행,열) ==>2차원배열
arr = np.arange(15)
print(arr)

arr = np.arange(15).reshape(3,5)
print(arr)

