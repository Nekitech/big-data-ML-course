import numpy as np

arr_1 = np.array([1, 5, 9, 11, 12, 2, 3, 4, 6])
arr_2 = np.array([2, 3, 4, 7, 9, 10, 12, 15])

print(np.intersect1d(arr_1, arr_2))