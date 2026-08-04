'''
Boolean Indexing (Most Used in Industry)
=> single condition
         - df[df["column"] > value]

=> multiple conditions
         - df[(df["column1" < value]) & (df["column2"] == value)]
   Always wrap each condition in parentheses.
   Logic operators for boolean indexing - AND (&), OR (|), NOT (~)
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

#Single condition
filter_age = df[df["Age"]>20]
print(filter_age)

delhi = df[df["City"]=="Delhi"]
print(delhi)

#Multiple conditions
rw = df[(df["City"] == "Delhi") & (df["Salary"] > 45000)]      # Returns Employees from Delhi and Salary > 45,000:
print(rw)     


rw = df[(df["City"] == "Delhi") | (df["Department"] == "AI")]  #Returns Employees from Delhi or Employees from AI Department
print(rw)

rw = df[~(df["Department"] == "AI")]                           #Returns All Employees not from AI Department
print(rw)