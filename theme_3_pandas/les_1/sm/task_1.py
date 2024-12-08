import pandas as pd

data = {
    'Name': ["Андрей", "Анна", "Василий", "Антон", "Екатерина", "Сергей", "Анастасия", "Иван", "Александр", "Михаил"],
    'Surname': ["Антонов", "Иванова", "Петров", "Попов", "Носкова", "Милютин", "Степанова", "Сидоров", "Попов", "Петров"],
    'Post': ["Директор", "Главный бухгалтер", "Инженер", "Инженер", "Экономист", "Водитель", "Зав.Хоз.", "Техник", "Программист", "Программист"],
    'Salary': [50000, 45000, 30000, 30000, 35000, 25000, 40000, 35000, 35000, 40000],
    'Age': [35, 30, 28, 27, 30, 25, 26, 33, 32, 27]
}
data_pandas = pd.DataFrame(data)

average_salary = data_pandas['Salary'].mean()

higher_salary_posts = data_pandas.loc[data_pandas['Salary'] > average_salary, 'Post'].unique()

lower_salary_posts = data_pandas.loc[data_pandas['Salary'] < average_salary, 'Post'].unique()

max_salary_employees = data_pandas.loc[data_pandas['Salary'] == data_pandas['Salary'].max(), ['Name', 'Surname']]

min_salary_employees = data_pandas.loc[data_pandas['Salary'] == data_pandas['Salary'].min(), ['Name', 'Surname']]

average_age = data_pandas['Age'].mean()

count_older = (data_pandas['Age'] > average_age).sum()

count_younger = (data_pandas['Age'] < average_age).sum()

youngest_employee = data_pandas.loc[data_pandas['Age'] == data_pandas['Age'].min()]

duplicates_counts = data_pandas['Surname'].value_counts()
duplicate_surnames = duplicates_counts[duplicates_counts > 1].sum()

print(data_pandas.sort_values(by='Salary', ascending=False))
print(f"1) Средняя зарплата сотрудников фирмы: {average_salary}")
print(f"2) Должности с зарплатой выше средней: {higher_salary_posts}")
print(f"3) Должности с зарплатой ниже средней: {lower_salary_posts}")
print(f"4) Сотрудники с максимальной зарплатой:\n{max_salary_employees}")
print(f"5) Сотрудники с минимальной зарплатой:\n{min_salary_employees}")
print(f"6) Средний возраст сотрудников фирмы: {average_age}")
print(f"7) Количество сотрудников старше среднего возраста: {count_older}")
print(f"8) Количество сотрудников младше среднего возраста: {count_younger}")
print(f"9) Данные о самом молодом сотруднике:\n{youngest_employee}")
print(f"10) Количество сотрудников с одинаковыми фамилиями: {duplicate_surnames}")
