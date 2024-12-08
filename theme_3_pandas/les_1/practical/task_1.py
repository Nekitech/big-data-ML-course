import pandas as pd

data = {
    "city": ["Тамбов", "Воронеж", "Липецк", "Рязань", "Курск"],
    "npeople": [0.26, 1.05, 0.49, 0.52, 0.44]
}

frame = pd.DataFrame(data, index=data["city"])
print(frame)

print(frame[frame.city == 'Тамбов'])

print(frame.drop("Рязань"))

print("Фильтрация по численности населения:", frame.sort_values(by="npeople", ascending=True))
print("Города, в которых численность населения больше 500 т.",frame[frame.npeople > 0.5])

print(frame.drop("city", axis=1))

