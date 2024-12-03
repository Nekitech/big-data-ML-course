import matplotlib.pyplot as plt

weight1 = [64, 55.8, 61.2, 60.45, 61]
height1 = [113.7, 157.7, 136, 148.9, 125.3]

weight2 = [61.9, 64, 62.1, 62.4, 63.6]
height2 = [135.1, 182.2, 195.9, 165.1, 125.1]

weight3 = [71.3, 70.8, 70, 71.1, 71.7]
height3 = [165.8, 192.8, 161.4, 181.1, 177.3]

plt.scatter(weight1, height1, color='blue', s=80, alpha=0.8, edgecolor='k', label='Group 1')
plt.scatter(weight2, height2, color='green', s=80, alpha=0.8, edgecolor='k', label='Group 2')
plt.scatter(weight3, height3, color='red', s=80, alpha=0.8, edgecolor='k', label='Group 3')

plt.legend(title='Группы', fontsize=10)

plt.title('Точечный график групп', fontsize=16)
plt.xlabel('Масса', fontsize=12)
plt.ylabel('Высота', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()
