import numpy as np

vector = np.arange(1, 17)
matrix = np.zeros((4, 4))


# 1 способ
for i in range(4):
    matrix[i] = vector[i * 4:(i + 1) * 4]

print(np.diag(matrix))

# 2 способ

matrix = vector.reshape(4, 4)
print(np.diag(matrix))