import matplotlib.pyplot as plt
import numpy as np

# Заданные данные
N = 7  # Количество групп
menMeans = (22, 27, 31, 32, 26, 35, 28)
womenMeans = (21, 36, 35, 34, 22, 39, 25)
menStd = (4, 3, 3, 2, 3, 5, 3)
womenStd = (3, 4, 3, 2, 3, 5, 2)

# Генерация позиций для столбцов
ind = np.arange(N)  # Позиции групп по оси X
width = 0.35        # Ширина столбцов

# Построение столбчатых диаграмм
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(ind - width/2, menMeans, width, yerr=menStd, label='Men', capsize=5)
rects2 = ax.bar(ind + width/2, womenMeans, width, yerr=womenStd, label='Women', capsize=5)

# Добавление заголовков и подписей
ax.set_title('Средние значения с погрешностями для мужчин и женщин')
ax.set_xlabel('Группы')
ax.set_ylabel('Средние значения')
ax.set_xticks(ind)
ax.set_xticklabels([f'Group {i+1}' for i in range(N)])
ax.legend()

# Отображение значений на столбцах
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # смещение вверх на 3 пикселя
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# Отображение диаграммы
plt.tight_layout()
plt.show()
