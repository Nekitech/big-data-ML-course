import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=12345)

draws = rng.standard_normal(100)

categories = pd.cut(draws, bins=[-np.inf, -1, 1, np.inf], labels=['low', 'medium', 'high'])

categorical_data = pd.Categorical(categories)

print("Категориальные данные:")
print(categorical_data)

category_counts = categorical_data.value_counts()

print("Количество значений по категориям:")
print(category_counts)
