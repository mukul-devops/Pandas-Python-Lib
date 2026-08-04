'''
We can update single value in Dataframe like this:
 df.loc[row_selection, column_selection] = value
'''
import pandas as pd
import numpy as np

data = {
    "EmployeeID":[101,102,103,104,105],
    "Name":["Mukul","Rahul","Aman","Priya","Neha"],
    "Age":[20,22,19,21,23],
    "Department":["AI","Web","AI","Data","Web"],
    "Salary":[60000,40000,42000,50000,48000],
    "Experience":[1,2,1,3,4]
}

df = pd.DataFrame(data)

#Update single value
df.loc[3,"Department"] = "AI"

#Update multiple value in single column
df.loc[[0,3],"Salary"] = 120000, 100000

#Using replace method: It is also used on entire DataFrame
df["Department"] = df["Department"].replace({"AI":"Artificial Intelligence" ,"Web":"Web Development"})
print(df["Department"])

#Update column:
df["Experience"] = df["Experience"]+5
print(df)

#Clip Values (Useful in ML)
#Limit salary between 30k and 40k
print(df["Salary"].clip(30000,50000))