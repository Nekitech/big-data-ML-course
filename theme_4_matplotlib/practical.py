import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('fdata.csv', delimiter=',')

data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%y')

plt.figure(figsize=(10,6))

plt.plot(data['Date'], data['Open'], label='Open', color='blue')
plt.plot(data['Date'], data['High'], label='High', color='green')
plt.plot(data['Date'], data['Low'], label='Low', color='red')
plt.plot(data['Date'], data['Close'], label='Close', color='black')

plt.title('Финансовые данные')
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
