import pandas as pd

data = pd.read_csv('employees.csv')

first_10_records = data.head(10)
print(first_10_records)

finded_names = data[data['first_name'].str.startswith('C', na=False)][['first_name', 'last_name', 'salary']]
print(finded_names)

departments_30_90 = data[data['department_id'].isin([30, 90])][['first_name', 'last_name', 'salary', 'department_id']]
print(departments_30_90)
