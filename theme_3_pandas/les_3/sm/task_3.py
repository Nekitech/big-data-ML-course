import pandas as pd

df = pd.read_excel('SaleData.xlsx')

# 3
pivot3 = pd.pivot_table(df, values='Sale_amt', index='Region', aggfunc='sum')

print(pivot3)