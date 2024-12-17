import pandas as pd

df = pd.read_excel('SaleData.xlsx')


# 4
home_theater_df = df[df['Item'] == 'Home Theater']
pivot4 = pd.pivot_table(home_theater_df,
                        values='Units',
                        index='Region',
                        aggfunc='sum')

print(pivot4)
