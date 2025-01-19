import pandas as pd

data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'Location': ['New York', 'Paris', 'Berlin', 'London'],
    'Age': [24, 13, 53, 33]

}

df  = pd.DataFrame(data)

df.index = ['a', 'b', 'c', 'd']

print(df)

# avec csv file 

file_path = 'data.csv'

df_csv  = pd.read_csv(file_path)

print(df_csv)
