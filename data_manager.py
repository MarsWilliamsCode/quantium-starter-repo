import pandas as pd

df0 = pd.read_csv('./data/daily_sales_data_0.csv')
df1 = pd.read_csv('./data/daily_sales_data_1.csv')
df2 = pd.read_csv('./data/daily_sales_data_2.csv')

combined_df = pd.concat([df0, df1, df2])

combined_df = combined_df.query('product == "pink morsel"')
combined_df['price'] = combined_df['price'].str.replace('$','')
combined_df['price'] = combined_df['price'].astype(float)

combined_df['sales'] = combined_df['price'] * combined_df['quantity']
print(combined_df.head())

combined_df.to_csv('./data/final_daily_sales_data.csv', columns=['sales', 'date', 'region'], index=False)





