import pandas as pd

df = pd.read_excel('SaleData.xlsx')

# 1
pivot1 = pd.pivot_table(df, values='Sale_amt', index='Region', columns='Manager', aggfunc='sum', fill_value=0)

print(pivot1)