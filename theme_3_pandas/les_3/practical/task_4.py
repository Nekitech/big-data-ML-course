import pandas as pd

file_path = 'titanic.csv'
titanic = pd.read_csv(file_path)

pivot_table = titanic.pivot_table(
    index=['class', 'sex'],
    columns=['alive'],
    values=['age', 'fare'],
    aggfunc='mean',
    margins=True,
    margins_name='Total'
)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(pivot_table)
