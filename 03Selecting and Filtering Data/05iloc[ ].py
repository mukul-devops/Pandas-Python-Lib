'''
-Selecting Rows with iloc[] property
 iloc[] selects by position.
   df.iloc[row_position, column_position]                
   row_ position   - row index(lable) like 0, [0,2,4], 1:3   *Important: Unlike loc, iloc excludes the ending position.
   column_position -   column lable(index) like 1, [0,1,2,5], 2:7


'''

import pandas as pd

data = {
    "CustomerID": [101, 102, 103, 104, 105],
    "Name": ["Mukul", "Rahul", "Aman", "Priya", "Neha"],  
    "Age": [20, 22, 19, 21, 23],
    "City": ["Delhi", "Jaipur", "Noida", "Delhi", "Chandigarh"],
    "Department": ["AI", "Web", "AI", "Data", "Web"],
    "Salary": [60000, 40000, 42000, 50000, 48000]
}

df = pd.DataFrame(data)

#select single row                          
print(df.iloc[0])                           

#select multiple row
print(df.iloc[[0,2,3]])

#select row with range
print(df.iloc[0:3])

#select specific columns
print(df.iloc[:,1])

print(df.iloc[:,2:7])                       # : → all rows.

print(df.iloc[[0,2,4],[0,1,2,5]])

