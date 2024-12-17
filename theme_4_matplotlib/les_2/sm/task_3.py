import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'diamonds.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
sns.histplot(df['carat'], bins=40, color='skyblue', kde=True)

plt.title('Распределение числовой переменной carat')
plt.xlabel('Вес бриллиантов (carat)')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

