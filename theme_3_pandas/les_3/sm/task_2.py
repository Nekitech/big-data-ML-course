import pandas as pd

df = pd.read_excel('SaleData.xlsx')

# 2
pivot2 = pd.pivot_table(df, values='Units', index='Region', aggfunc='sum')

print(pivot2)