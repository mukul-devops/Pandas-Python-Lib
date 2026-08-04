'''
query() is method which Filter rows in a DataFrame using a string expression (like SQL-style queries).
Syntax - Single condition
        - df.query("column_name > value")
        
        multi-condition
        df.query("age > 23 and city == 'Delhi'")

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

# df[df["Salary"] > 45000]

#Single condition
Filter_row = df.query("Salary > 45000")
print(Filter_row)

Filter_row = df.query("not Salary >= 42000")
print(Filter_row)

#Multiple conditions
Filter_row = df.query("Department == 'AI' and Salary >= 42000")
print(Filter_row)
#Many people find query() easier to read for complex filters.




