import pandas as pd

file_path = 'ufo.csv'
ufo = pd.read_csv(file_path)
pd.set_option('display.max_rows', None)
print(ufo.groupby(["country", "date_documented"]).size())
