'''
-Both loc[] and iloc[] are indexers used to access rows and columns in a DataFrame
-Selecting Rows with loc[] property
 loc[] selects by label (index name).
   df.loc[row_selection, column_selection]
   
   row selection    - row index(lable) like 0, [0,2,4], 1:3  *Important: loc includes the ending label.
   column selection - columns like "Name" ,["Name","Age","Salary"]
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
print(df.loc[0])

#select multiple row
print(df.loc[[0,2,3]])

#select row with range
print(df.loc[0:3])

#select specific column
print(df.loc[:,"Name"])                       # : → all rows.

#select row with specific columns
print(df.loc[[0,2,3],["City","Name"]])

#Selecting Specific Columns After Filtering

#Find Delhi employees and display only their names and salaries:
df.loc[df["City"] == "Delhi", ["Name", "Salary"]]