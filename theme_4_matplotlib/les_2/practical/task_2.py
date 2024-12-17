import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла diamonds.csv
file_path = 'diamonds.csv'
df = pd.read_csv(file_path)

# Сортировка данных по весу (carat) для корректного отображения графика
df_sorted = df.sort_values(by='carat')

# Построение линейного графика: carat (вес) на оси X, price (цена) на оси Y
plt.figure(figsize=(30, 6))
plt.plot(df_sorted['carat'], df_sorted['price'], color='blue', linestyle='-', marker='o', markersize=3)

# Добавляем заголовки и подписи осей
plt.title('Зависимость цены бриллиантов от веса')
plt.xlabel('Вес (carat)')
plt.ylabel('Цена (price)')

# Отображение сетки для удобства чтения графика
plt.grid(True)

# Отображаем линейный график
plt.show()
