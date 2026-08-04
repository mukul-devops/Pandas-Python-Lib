'''
df.head()   -> View the First Few Rows    
df.tail()   -> View the Last Few Rows
By default, head() and tail() display the first and last 5 rows of the DataFrame, respectively.
You can also specify the number of rows to display as df.head(n) or df.tail(n)
'''
import pandas as pd
df = pd.read_csv("sample.csv")  # Load the CSV file into a DataFrame

#These are some methods used to access rows from DataFrame
print(df.head())  # Display the first 5 rows of the DataFrame
print(df.tail())  # Display the last 5 rows of the DataFrame

print(df.head(3))  # Display the first 3 rows of the DataFrame
print(df.tail(9))  # Display the last 9 rows of the DataFrame

#Sample() is a method used to access random n number of row
print(df.sample())  #Display a random row of the DataFrame
print(df.sample(6)) #Display the 6 random row of the DataFrame