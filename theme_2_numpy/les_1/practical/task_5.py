import numpy as np

arr = np.zeros((4, 5))

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        arr[i][j] = np.random.choice([0, 1, 2, 3])

print(arr)
arr_t = arr.T
print(np.dot(arr, arr_t))