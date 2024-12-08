import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(0, 10, size=(3, 5)), columns=list('ABCDE'))
df2 = pd.DataFrame(np.random.randint(0, 10, size=(4, 4)), columns=list('ABCD'))

print("DataFrame 1 (3x5):")
print(df1)

print("\nDataFrame 2 (4x4):")
print(df2)

result = df1.add(df2, fill_value=-1)

print("\nРезультат сложения с заменой отсутствующих значений на -1:")
print(result)
