

import pandas as pd


df=pd.read_excel('123.xlsx')
print(df.shape)
df=df.dropna()
print(df.shape)
a=df.drop_duplicates()
print(a.shape)
a.to_excel("321.xlsx")