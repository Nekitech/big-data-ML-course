import pandas as pd
import matplotlib.pyplot as plt

file_path = 'diamonds.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=50, color='skyblue', edgecolor='black')

plt.title('Гистограмма распределения бриллиантов по цене')
plt.xlabel('Цена')
plt.ylabel('Кол-во')

plt.show()
