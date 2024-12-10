import pandas as pd

data = pd.DataFrame({"name": ["Михаил", "Матвей", "Михаил", "Антон", "Сергей"],
                     "value": [3, 4, 4, 5, 5]})  # в данном объекте нет дупликатов

print(data)
data_no_duplicates = data.drop_duplicates()
print(data_no_duplicates)
