import pandas as pd
import numpy as np

data = pd.DataFrame([
    [1.2, 3.7, 4.8, 2.2],
    [0.3, np.nan, 8.8, np.nan],
    [np.nan, np.nan, np.nan, np.nan]
])
print(data)

data_no_nan = data.dropna()
print("DataFrame без строк с отсутствующими значениями:")
print(data_no_nan)


data_filled = data.copy()

for col in data.columns:
    for row in data.index:
        if pd.isna(data.at[row, col]):
            value = float(input(f"Введите значение для замены отсутствующего элемента в строке {row}, столбце {col}: "))
            data_filled.at[row, col] = value

print("DataFrame с заменой отсутствующих значений:")
print(data_filled)
