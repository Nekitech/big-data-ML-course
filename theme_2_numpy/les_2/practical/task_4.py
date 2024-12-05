import numpy as np

mx = np.random.standard_normal((4, 5))
rows = np.arange(mx.shape[0])
print(mx)
print(mx[rows].sum(axis=1))