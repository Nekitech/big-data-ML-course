import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'titanic.csv'
df = pd.read_csv(file_path)

sns.set(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.countplot(x='survived', hue='survived', data=df, palette='muted', legend=False)

plt.title('Количество выживших и погибших пассажиров Титаника')
plt.xticks([0, 1], ['Погибшие', 'Выжившие'])
plt.xlabel('Статус')
plt.ylabel('Количество пассажиров')

plt.show()

plt.figure(figsize=(10, 6))

sns.histplot(data=df, x='age', hue='survived', kde=True, palette='Set2',  bins=30)
plt.title('Распределение возраста у выживших и погибших пассажиров')
plt.xlabel('Возраст')
plt.ylabel('Количество пассажиров')
plt.legend(title='Статус', labels=['Погибшие', 'Выжившие'])
plt.show()

plt.figure(figsize=(10, 6))
sns.catplot(x='class', hue='sex', col='survived', data=df, kind='count', palette='pastel')
plt.subplots_adjust(top=0.85)
plt.suptitle('Распределение выживших и погибших по классу и полу')
plt.show()
