'''
- df["column"].unique() is a method used to get a series of unique values of a column

- df["Department"].value_counts() is a method used to get number of unique values in a column
        Works on a Series.
        Returns a new Series showing the frequency of unique values.
        This is super handy for categorical data analysis (like counting genres in your Netflix dataset).

- df[Department].values
        Returns the underlying data of a Series or DataFrame as a NumPy array.
        Useful when you just want the raw values without labels.

- df[Department].index
        Returns the index (labels) of a Series or DataFrame
'''

import pandas as pd
import numpy as np

data = {
    "ID": [1,2,3,4,5,5,6],
    "Name": ["Mukul","Rahul","Aman","Priya","Neha","Neha","  Mohit  "],
    "Age": [20,np.nan,19,21,23,23,25],
    "Salary": [60000,40000,42000,np.nan,48000,48000,"55000"],
    "Department": ["AI","Web","AI","Data","Web","Web","AI"],
    "City": ["Delhi","Jaipur","Noida","Delhi","Delhi","Delhi","Mumbai"]
}

df = pd.DataFrame(data)

print(df["Salary"].unique())


#Count Categories
data = df["Department"].value_counts()
print(data)
print(data.values)
print(data.index)