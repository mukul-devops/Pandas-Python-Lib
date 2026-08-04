'''
- transform() performs an operation on each group and
  returns a result with the same number of rows as the original DataFrame.

- Simple rule to remember
   agg() → reduces rows (summary)
    Returns one value per group.

   transform() → keeps all rows
    Returns one value for every original row with same index.

- Common Functions with transform()
    .transform("sum")
    .transform("mean")
    .transform("max")
    .transform("min")
    .transform("count")
    .transform("rank")
    .transform(lambda x: ...)
'''

import pandas as pd

df = pd.DataFrame({
    "Name": ["Mukul", "Rahul", "Priya", "Neha", "Raj", "Simran", "Ankit", "Pooja"],
    "Age":[20,19,18,19,21,18,20,20],
    "Department": ["IT", "HR", "IT", "HR", "Finance", "IT", "Finance", "HR"],
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Delhi", "Mumbai", "Delhi"],
    "Salary": [90000, 40000, 60000, 45000, 70000, 55000, 75000, 42000],
    "Experience": [2, 3, 5, 2, 8, 4, 7, 1]
})

print(df.groupby("Age")["Salary"].transform("mean"))

#Percentage of Department Salary
df["Department_Total"] = (
    df.groupby("Department")["Salary"]
      .transform("sum")
)

df["Salary_Percentage"] = (
    df["Salary"] / df["Department_Total"] * 100
)
print(df)

#Fill Missing Values

#Suppose one salary is missing.
df.loc[2, "Salary"] = None

#Fill it with the department average:
df["Salary"] = (
    df.groupby("Department")["Salary"]
      .transform(lambda x: x.fillna(x.mean()))
)
print(df["Salary"])
