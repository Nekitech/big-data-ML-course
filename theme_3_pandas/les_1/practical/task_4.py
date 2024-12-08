import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(4, 4)), columns=list('ABCD'))

print(df)

row_means = df.apply(np.mean, axis=1)

print(row_means)
