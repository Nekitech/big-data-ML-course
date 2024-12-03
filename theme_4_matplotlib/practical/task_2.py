# 2. Написать скрипт для построения линий с разными стилями для наборов данных:
#
# x1 = [10,12,15]
#
# y1 = [25,18,9]
#
# x2 = [10,30,20]
#
# y2 = [40,20,30]

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

plt.plot([10,12,15], [25,18,9], color='blue')
plt.plot([10,30,20], [40,20,30], color='red', linestyle='dashed')

plt.xlabel('x coord')
plt.ylabel('y coord')

plt.show()
