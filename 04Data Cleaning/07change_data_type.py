'''
- .astype() method is used to convert data type (Most Common)

-pd.to-numeric(df["Column"], error="coerce") used to change data type into num(int,float) 
 and also replace invalid values with nan (Recommended for Real Data)
 If your data may contain invalid values like "N/A" or "abc", a safer approach is:

 df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

 Invalid values become NaN, which you can then handle with fillna() or dropna().
'''

import pandas as pd
import numpy as np

data = {
    "ID": [1,2,3,4,5,5,6],
    "Name": ["Mukul","Rahul","Aman","Priya","Neha","Neha","  Mohit  "],
    "Age": [20,np.nan,19,21,23,23,25],
    "Salary": [60000,40000,42000,"50000",48000,48000,"55000"],
    "Department": ["AI","Web","AI","Data","Web","Web","AI"],
    "City": ["Delhi","Jaipur","Noida","Delhi","Delhi","Delhi","Mumbai"]
}

df = pd.DataFrame(data)

print(df.dtypes)   #Shows Salary object

df["Salary"] = df["Salary"].astype(float)
print(df)
