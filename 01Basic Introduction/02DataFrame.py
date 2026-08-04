'''
A DataFrame is like an Excel sheet with rows and columns.
A DataFrame is essentially a collection of aligned Series objects that share the same index.
'''

import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 28],
    "Salary": [40000, 65000, 50000]
}

df = pd.DataFrame(data)
print(df)


#Creating a DataFrame from Different Sources

#From a Dictionary of Lists
df = pd.DataFrame({
    "Name": ["Mukul", "Karan", "Rohit"],
    "Age": [20, 19, 21],
    "Std": ["1st year", "1st year", "2nd year"]
})

print(df)

# From a List of Lists
df = pd.DataFrame([
    ["Mukul", 20, "1st year"],
    ["Karan", 19, "1st year"],
    ["Rohit", 21, "2nd year"]
], columns=["Name", "Age", "Std"])

print(df)

#From a List of Dictionaries
df = pd.DataFrame([
    {"Name": "Mukul", "Age": 20, "Std": "1st year"},
    {"Name": "Karan", "Age": 19, "Std": "1st year"},
    {"Name": "Rohit", "Age": 21, "Std": "2nd year"}
])

print(df)


# These are some functions to access the data in a DataFrame:
print(df["Name"])

print(df["Age"])

print(type(df))

print(type(df["Age"]))