import numpy as np

ages = np.array([25, 30, 35, 25, 40, 30, 25, 35, 30, 40])

names = np.array(["Анна", "Борис", "Анна", "Виктор", "Глеб",
                  "Анна", "Дмитрий", "Виктор", "Глеб", "Борис"])

target_name = input('Введите имя: ')

result = ages[names == target_name]

print(f"Возраст сотрудников с именем '{target_name}':", result)
