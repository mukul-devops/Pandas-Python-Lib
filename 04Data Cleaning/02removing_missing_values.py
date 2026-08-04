'''
df.dropna()
 Rows having missing values are removed.

df.dropna(axis = 1)
 Drop Specific Columns containing  NaN            axis=0 → Rows (default)
                                                  axis=1 → Columns
df.dropna(subset=[c1,c2...])         
                                        
   subset=['col1','col2'] → check only specific columns.

# Most Pandas methods return a new DataFrame.
  df.dropna(inplace=True),   But after seting inplace = True method affected orginal DtatFrame(Original df changed)

In modern Pandas code, many developers prefer:
df = df.dropna()
instead of inplace=True, because it is clearer and works consistently with method chaining.

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

#Drop Rows with Missing Data
print(df.dropna())           

#Drop Specific Columns with Missing Data
df.dropna(axis=1,inplace= True)   #inplace = True , make changes on orginal df
print(df)