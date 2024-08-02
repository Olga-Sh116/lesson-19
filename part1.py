import pandas as pd


df = pd.read_csv('scraped_company_data.csv')
print (df.describe())
print (df.info())
print (df.head(5))


#ps-ratio