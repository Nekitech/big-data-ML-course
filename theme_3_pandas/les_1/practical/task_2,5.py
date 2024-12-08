import pandas as pd

data = {
    'Name': ["Андрей", "Анна", "Василий", "Антон", "Екатерина", "Сергей", "Анастасия", "Иван", "Александр", "Михаил"],
    'Surname': ["Антонов", "Иванова", "Петров", "Попов", "Носкова", "Милютин", "Степанова", "Сидоров", "Попов", "Петров"],
    'Post': ["Директор", "Главный бухгалтер", "Инженер", "Инженер", "Экономист", "Водитель", "Зав.Хоз.", "Техник", "Программист", "Программист"],
    'Salary': [50000, 45000, 30000, 30000, 35000, 25000, 40000, 35000, 35000, 40000],
    'Age': [35, 30, 28, 27, 30, 25, 26, 33, 32, 27]
}

df = pd.DataFrame(data)

print("Исходный DataFrame:")
print(df)

sorted_df = df.sort_values(by='Salary')

print("\nDataFrame, отсортированный по столбцу 'Salary':")
print(sorted_df)

selection_loc = sorted_df.loc[sorted_df['Salary'] > 35000, ['Name', 'Salary']]
print("Выборка с использованием loc (зарплата > 35000):")
print(selection_loc)


selection_iloc = sorted_df.iloc[:3, [0, 3]]
print("\nВыборка с использованием iloc (первые три строки, столбцы Name и Salary):")
print(selection_iloc)

