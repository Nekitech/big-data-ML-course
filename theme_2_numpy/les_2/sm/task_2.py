import numpy as np
import numpy.linalg as la

mx = np.random.standard_normal((5, 5))

print(mx)
print(la.det(mx))
print(la.inv(mx))