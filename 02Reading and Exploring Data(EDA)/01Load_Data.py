import pandas as pd
# CSV
df = pd.read_csv("sample.csv")     #if unicode decoding error occurs, use encoding='utf-8' or encoding='latin1' as an argument in read_csv function
print(df)

# Excel
df = pd.read_excel("SampleSuperstore.xlsx")
print(df)

# JSON
df = pd.read_json("sample_Data.json")
print(df)

# SQL database
# df = pd.read_sql(query, connection)
