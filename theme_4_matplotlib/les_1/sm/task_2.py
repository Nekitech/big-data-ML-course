import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 800)
func_1 = np.sin(x)
func_2 = x
func_3 = x**2

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

ax1.plot(x, func_1, color='blue', label='sin(x)')
ax1.set_title('График функции sin(x)', fontsize=14)
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(fontsize=10)

ax2.plot(x, func_2, color='green', label='x', linestyle='--')
ax2.set_title('График функции x', fontsize=14)
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(fontsize=10)


ax3.plot(x, func_3, color='red', label='x^2', linestyle='-.')
ax3.set_title('График функции x^2', fontsize=14)
ax3.set_xlabel('x', fontsize=12)
ax3.set_ylabel('y', fontsize=12)
ax3.grid(True, linestyle='--', alpha=0.6)
ax3.legend(fontsize=10)

plt.tight_layout()
plt.show()
