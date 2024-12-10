import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.standard_normal((1000, 5)), columns=['A', 'B', 'C', 'D', 'E'])


filtered_data = data[(data > 2).any(axis=1)]

print("DataFrame без строк с выбросами (> 2):")
print(filtered_data.head())

filtered_data_all = data[(data <= 2).all(axis=1)]

print("DataFrame, где все значения <= 2:")
print(filtered_data_all.head())
