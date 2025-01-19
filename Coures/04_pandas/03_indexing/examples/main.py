"""
Index and select data from pandas DataFrame:
    - Square brackets
    - .loc[]
    - .iloc[]


"""

import pandas as pd

df = pd.read_csv('data.csv')

df.index = ['FR', 'GE', 'IT', 'SP', 'UK']

print(df)

# access colum by name -> Series 
country = df['country']
print(country)
print(type(country))
print(country['FR'])


# access column by name -> DataFrame
country_df = df[['country']]
print(df[['country']])
print(type(df[['country']]))


sub_df = df[['country', 'capital']]
print(sub_df)

# slicing rows 
print(df[1:3])

print('-----------------')
info_fr_series  = df.loc['FR'] # FR 
print(info_fr_series)
print(type(info_fr_series))
print(dict(info_fr_series))

# for DF 
info_fr_df = df.loc[['FR']]
print(info_fr_df)
print(type(info_fr_df))


# df.loc[[row1 , row2 , row3]] 
# df.loc[:, [col1 , col2 , col3]] ~ df[[col1 , col2 , col3]]
# df.loc[ [row1 , row2 , row3] , [col1, col2, col3] ]

print(type(df.loc[['FR'], ['country']]))
