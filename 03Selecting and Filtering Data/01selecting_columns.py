'''
=>Selcting single column 
                    - df["Column"]                        ~ output is Series

=>Slecting Multiple Columns
  Use double square brackets:
                    - df[["Column1", "Coulmn2", ...]]      ~ output is DataFrame

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
print(df["City"])

#Notice the output is a Series.
print(type(df["City"]))

multi_columns = df[["Name", "Salary"]]
print(multi_columns)

#Here, output is DataFrame
print(type(multi_columns))