'''
- df.drop() is a method used to remove rows and columns in DataFrame
- df.drop(cloumns=["column1",column2], index=[1,3,4])
  
'''

import pandas as pd

data = {
    "EmployeeID":[101,102,103,104,105],
    "Name":["Mukul","Rahul","Aman","Priya","Neha"],
    "Age":[20,22,19,21,23],
    "Department":["AI","Web","AI","Data","Web"],
    "Salary":[60000,40000,42000,50000,48000],
    "Experience":[1,2,1,3,4]
}

df = pd.DataFrame(data)

#Remove one column:
print(df.drop(columns="Experience"))


#Remove multiple columns:
print(df.drop(columns=["Experience","Age"]))


#Remove row with index 2:
print(df.drop(index=2))

#Remove multiple rows:
print(df.drop(index=[1,3]))

#Remove row and column:
print(df.drop(columns=["Experience","Age"],index=2))
