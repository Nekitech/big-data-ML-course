import numpy as np

names = np.array(['Иван', 'Анна', 'Петр', 'Иван', 'Ольга', 'Анна', 'Дмитрий', 'Ольга', 'Екатерина'])

unique_sorted_names = np.sort(np.unique(names))

print(unique_sorted_names)
