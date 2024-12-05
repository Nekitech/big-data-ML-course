import numpy as np

vector = np.arange(1, 37)

mx = vector.reshape(6,6)
sum_cols = mx.sum(axis=0)
print(sum_cols)

sum_rows = mx.sum(axis=1)
print(sum_rows)

print(mx)