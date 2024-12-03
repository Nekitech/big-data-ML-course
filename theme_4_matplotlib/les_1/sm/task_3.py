import numpy as np
import matplotlib.pyplot as plt

n_groups = 5
pm_means = (25, 34, 27, 36, 21)
m_means = (24, 37, 20, 32, 29)
f_means = (23, 32, 36, 39, 22)

index = np.arange(n_groups)
bar_width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(index, pm_means, bar_width, label='Прикладная информатика', color='blue')
bars2 = ax.bar(index + bar_width, m_means, bar_width, label='Физика', color='green')
bars3 = ax.bar(index + 2 * bar_width, f_means, bar_width, label='Математика', color='red')

ax.set_title('Сравнение баллов по группам и специальностям', fontsize=14)
ax.set_xlabel('Группы', fontsize=12)
ax.set_ylabel('Баллы', fontsize=12)
ax.set_xticks(index + bar_width)  # Установка меток по центру групп
ax.set_xticklabels([f'Group {i+1}' for i in range(n_groups)])
ax.legend(fontsize=10)

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
