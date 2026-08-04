'''
df.info()   -> Display a concise summary of the DataFrame
The info() method provides information about the DataFrame,
notably the number of rows and columns,
including the number of non-null entries,
the data types of each column, and memory usage.
'''
import pandas as pd

df = pd.read_csv("sample.csv")  # Load the CSV file into a DataFrame
df.info()

