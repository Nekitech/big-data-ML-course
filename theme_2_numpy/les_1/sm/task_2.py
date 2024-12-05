import numpy as np

mx = np.ones((8, 8))
mx[1::2, 1::2] = 5
mx[0::2, 0::2] = 5
print(mx)