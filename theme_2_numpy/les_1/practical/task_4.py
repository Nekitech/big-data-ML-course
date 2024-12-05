import numpy as np

arr = np.zeros((8, 8))

for i in range(8):
    for j in range(8):
        arr[i][j] = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

cols = np.arange(8)
diag_1 = np.diag(arr)
diag_2 = np.diag(np.fliplr(arr))
print(arr)
print('искомые диагонали: ', diag_1, diag_2)