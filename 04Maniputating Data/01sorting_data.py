'''
-df.sort_value(by=column, ascending=True)
  ascending is by default True, and set False to get opposite response

- #Sort by Multiple Columns
    print(df.sort_values(
        by=["column1","column2"],
        ascending=[True,False]
    ))

    for string ascending order is (A-Z)
    sort_values() gives priority to 1 column then 2nd...
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

#Sort by Salary (Ascending)
print(df.sort_values(by="Salary"))

#Descending order
print(df.sort_values(by="Salary", ascending=False))

#Sort by Multiple Columns
print(df.sort_values(
    by=["Department","Salary"],
    ascending=[True,False]
))
#First sort by Department (A → Z).
#Within each department, sort Salary from highest to lowest.
