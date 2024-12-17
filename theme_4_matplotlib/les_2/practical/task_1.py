import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла diamonds.csv
file_path = 'diamonds.csv'
df = pd.read_csv(file_path)

# Построение гистограммы для столбца price (цена бриллиантов)
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=50, color='skyblue', edgecolor='black')

# Добавляем заголовки и подписи осей
plt.title('Гистограмма распределения бриллиантов по цене')
plt.xlabel('Цена')
plt.ylabel('Кол-во')

# Отображаем гистограмму
plt.show()
