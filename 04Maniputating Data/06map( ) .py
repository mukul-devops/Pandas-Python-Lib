'''
map() is used to replace or transform values in a single column(series).

Syntax:
-Series.map(function_or_dictionary)
'''

import pandas as pd

data = {
    "EmployeeID":[101,102,103,104,105],
    "Name":["Mukul","Rahul","Aman","Priya","Neha"],
    "Age":[20,22,19,21,23],
    "Gender":["M","M","M","F","F"],
    "Department":["AI","Web","AI","Data","Web"],
    "Salary":[60000,40000,42000,50000,48000],
    "Experience":[1,2,1,3,4]
}

df = pd.DataFrame(data)

#With Dictionary
df["Gender"] = df["Gender"].map({"M":"Male","F":"Female"})

#With Function
df["Experience"] = df["Experience"].map(lambda x: x + 2)

print(df)
