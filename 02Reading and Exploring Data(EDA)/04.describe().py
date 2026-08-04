'''
describe() is a method used to access statistics of the dataframe
count: Number of non-missing values.
mean: Average.
std: Standard deviation (how spread out the data is).
min/max: Smallest and largest values.
25%, 50%, 75%: Quartiles after data shortout that help understand the distribution.
like - A Shortout column = [22,23,24,25,26,27,28]
it's 25%, 50%, 75% = 23.5, 25, 26.5
'''
import pandas as pd
df = pd.read_csv("sample.csv")  

print(df.describe())
