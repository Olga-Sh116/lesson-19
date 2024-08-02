import pandas as pd


'''df = pd.read_csv('scraped_company_data.csv')
print (df.describe())
print (df.info())
print (df.head(5))'''

df = pd.read_csv('dz.csv')
df.fillna(0, inplace=True)

print(df)
group = df. groupby ('City')['Salary'].mean()
print(group)

df.to_csv('output.csv', index=False)
