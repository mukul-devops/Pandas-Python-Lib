'''
df.shape   -> gives (rows,columns)
df.columns -> gives column names
'''
import pandas as pd
df = pd.read_csv("sample.csv")

#These are some properties of DataFrame
print(df.shape)           #output: (94, 5)
print(df.columns)         #output: Index(['CsvID', 'Name', 'Email', 'Age', 'Country'], dtype='str')

#Convert to a list if needed:
#This is useful when you want to rename or select columns programmatically.
print(list(df.columns))   #output: ['CsvID', 'Name', 'Email', 'Age', 'Country']


print(df.index)           #output: RangeIndex(start=0, stop=94, step=1)
print(df.dtypes)          #output: CsvID      int64
                          #        Name         str
                          #        Email        str
                          #        Age        int64
                          #        Country      str
                          #        dtype: object