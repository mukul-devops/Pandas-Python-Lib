'''
-df.duplicate() meathod is used to detect duplicate rows in DataFrame, It Return boolean Series denoting duplicate rows.
-To find duplicates on specific column(s), use subset.
>>> df.duplicated(subset=["Column"])

-df.drop_duplicate() method used to remove duplicate rows

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

print(df.duplicated())

#Count Duplicates
print(df.duplicated().sum())

#Remove Duplicates
df.drop_duplicates(inplace=True)
print(df)