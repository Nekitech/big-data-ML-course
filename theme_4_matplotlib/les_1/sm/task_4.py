import matplotlib.pyplot as plt

labels = [ 'M', 'S', 'P', 'U', 'W']
val = [20.2, 19.6, 11.8, 19.3, 3.5]
explode = (0, 0.2, 0, 0, 0)

colors = ['blue', 'green', 'red', 'orange', 'yellow']

plt.pie(
    val,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    shadow=True,
    startangle=90
)

plt.title('Круговая диаграмма', fontsize=14)

plt.show()