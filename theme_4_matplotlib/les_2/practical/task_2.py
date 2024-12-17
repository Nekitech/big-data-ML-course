import pandas as pd
import matplotlib.pyplot as plt

file_path = 'diamonds.csv'
df = pd.read_csv(file_path)

df_sorted = df.sort_values(by='carat')

plt.figure(figsize=(30, 6))
plt.plot(df_sorted['carat'], df_sorted['price'], color='blue', linestyle='-', marker='o', markersize=3)

plt.title('Зависимость цены бриллиантов от веса')
plt.xlabel('Вес (carat)')
plt.ylabel('Цена (price)')

plt.grid(True)
plt.show()
