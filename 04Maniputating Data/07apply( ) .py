'''
- apply() function in Pandas is a versatile method that lets you apply a function along either axis of a DataFrame (rows or columns) 
  or to each element of a Series. 
  It’s more general than map() and works for both DataFrames and Series.

- df.apply(func,axis=0) 
 func: Function to apply (can be Python function, NumPy function, or lambda).

  axis:
  0 → Apply function to each column.
  1 → Apply function to each row.

- s.apply(Func)



'''

import pandas as pd

data = {
    "ID":[101,102,103,104,105],
    "Name":["Mukul","Rahul","Aman","Priya","Neha"],
    "Age":[20,17,19,18,14],
    "Gender":["M","M","M","F","F"],
    "Department":["AI","Web","AI","Data","Web"],
    "Salary":[60000,40000,42000,50000,48000],
    "Experience":[1,2,1,3,4]
}

df = pd.DataFrame(data)

#Apply lambda func
df["ID"] = df["ID"].apply(lambda x: x**2)


#Apply own func
def category(age):
    if age >= 18:
        return "Adult"
    else:
        return "Child"

df["Age"] = df["Age"].apply(category)

print(df)

#apply() on Multiple Columns
df = pd.DataFrame({
    "Math": [80, 70, 90],
    "Science": [75, 60, 95]
})

df["Total"] = df[["Math", "Science"]].apply(sum, axis=1)

print(df)



'''
When to Use Which?
Use map() when:
Replacing values (e.g., "M" → "Male").
Mapping categories using a dictionary.
Performing simple transformations on a single column.
Use apply() when:
You need custom logic with if-else.
You want to work with multiple columns.
You need row-wise or column-wise calculations.
You're creating new features for machine learning.
'''