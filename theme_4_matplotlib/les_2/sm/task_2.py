import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'ufo.csv'
df = pd.read_csv(file_path)

df['length_of_encounter_seconds'] = pd.to_numeric(
    df['length_of_encounter_seconds'],
    errors='coerce')
df = df.dropna(subset=['length_of_encounter_seconds'])

# Построение гистограммы распределения времени наблюдения
plt.figure(figsize=(10, 6))
sns.histplot(df['length_of_encounter_seconds'], bins=50, color='skyblue')
plt.title('Распределение времени наблюдения НЛО')
plt.xlabel('Время наблюдения (в секундах)')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
