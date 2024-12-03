import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)

y1 = np.sin(x)
y2 = x
y3 = x**2

plt.figure(figsize=(10, 6))  # Размер графика

plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-')
plt.plot(x, y2, label='x', color='green', linestyle='--')
plt.plot(x, y3, label='x^2', color='red', linestyle='-.')

plt.title('Графики функций sin(x), x и x^2', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.6)

plt.legend(fontsize=10, loc='upper right')

plt.tight_layout()
plt.show()
