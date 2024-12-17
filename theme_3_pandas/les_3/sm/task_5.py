import pandas as pd

df = pd.read_excel('SaleData.xlsx')


# 5
pivot5 = pd.pivot_table(df, values='Sale_amt', index='Item', aggfunc='max')

print(pivot5)
