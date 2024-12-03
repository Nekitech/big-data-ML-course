import matplotlib.pyplot as plt
import numpy as np

people = ('G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8')
segments = 4
data = np.array([
    [3.40022085, 7.70632498, 6.4097905, 10.51648577, 7.5330039, 7.1123587, 12.77792868, 3.44773477],
    [11.24811149, 5.03778215, 6.65808464, 12.32220677, 7.45964195, 6.79685302, 7.24578743, 3.69371847],
    [3.94253354, 4.74763549, 11.73529246, 4.6465543, 12.9952182, 4.63832778, 11.16849999, 8.56883433],
    [4.24409799, 12.71746612, 11.3772169, 9.00514257, 10.47084185, 10.97567589, 3.98287652, 8.80552122]
])

bar_width = 0.6
x = np.arange(len(people))

bottom = np.zeros(len(people))  # массив с нулями для хранения предыдущих высот столбца
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(segments):
    ax.bar(x, data[i], bar_width, label=f'Segment {i + 1}', bottom=bottom, color=colors[i])
    # добавление меток
    for j in range(len(people)):
        value = data[i][j]
        # для центрирования по вертикали берем высоту предыдущего куска столбца и суммируем его с высотой новой, деленной пополам
        ax.text(
            float(x[j]),
            float(bottom[j] + value / 2),
            f'{value:.1f}',
            ha='center',
            va='center',
            fontsize=9)
    bottom += data[i]

ax.set_xlabel('Peoples')
ax.set_ylabel('Values')

ax.set_xticks(x)
ax.set_xticklabels(people)
ax.legend()

plt.tight_layout()
plt.show()
