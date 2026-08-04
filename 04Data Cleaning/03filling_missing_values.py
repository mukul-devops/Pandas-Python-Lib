'''
Instead of deleting data, we often replace missing values.
.fillna() is a method used to replace missing values (NaN) in a DataFrame or Series 
 with a specified value or strategy.
#Fill missing value with 0 in whole DataFrame
 df.fillna(0)

#Column-specific replacement:
   df.fillna({"column1": value, "column2": value,...})

   Not useful but atleast know  
        Forward fill (propagate previous value):
        df.ffill()    , fills NaN with the last valid value
        Backward fill (use next value):
        df.bfill()    , fills NaN with the next valid value
   
'''


import pandas as pd
import numpy as np

data = {
    "ID": [1,2,3,np.nan,5,5,6],
    "Name": ["Mukul","Rahul",None,"Priya","Neha","Neha","  Mohit  "],
    "Age": [20,np.nan,19,21,23,23,25],
    "Salary": [60000,40000,42000,np.nan,48000,48000,55000],
    "Department": ["AI","Web","AI",np.nan,"Web","Web","AI"],
    "City": ["Delhi",None,"Noida","Delhi","Delhi","Delhi","Mumbai"]
}

df = pd.DataFrame(data)

# Fill with Zero
df["ID"] = df["ID"].fillna(0)

#Fill with Mean (Most Common)
df["Age"] = df["Age"].fillna(df["Age"].mean())

#Fill with Median
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Fill Text Columns
df["Department"] = df["Department"].fillna("Unknown")

#Column-specific replacement:
df = df.fillna({ "Name": "Unknown", "City":"city"})
print(df)