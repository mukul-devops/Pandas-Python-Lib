'''
- agg(["sum","max",....]) is used to apply many operation on each group at a time 
  by passing list of aggregation functions as a string.

- agg({"column1":"sum","column2":"max",..})
  also apply different aggregation function on different column by passing dictionary of "column":"aggregation" pairs


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

#Basic Aggregation

print(df["Salary"].sum())      #Give total salary.

print(df["Salary"].max())      #Give Maximum salary

print(df["Salary"].min())      #Give Minimum salary

print(df["Salary"].count())    #Count total rows.

print(df["Salary"].mean())     #Mean (Average) of salary

print(df["Salary"].median())   #Medain of salary(the middle value in a data set when the numbers are sorted from smallest to largest)

print(df["Salary"].mode())     #Mode of salary (the value that appears most frequently in a given set of data)

print(df["Salary"].std())      #Measures how spread out the salaries are from the average (mean).

print(df["Salary"].var())      #Variance is the square of standard deviation.

print(df["Salary"].nunique())  #Number of Unique Values

print(df["Salary"].unique())   #Give Unique Values


#Multiple Aggregations with groupby
print(df.groupby("Department")["Salary"].agg(["sum", "mean", "min", "max", "count"]))

#Different Aggregations for Different Columns
result = df.groupby("Department").agg({
    "Salary": "mean",
    "Experience": "max"
})
print(result)

#Multiple Functions on Multiple Columns
result = df.groupby("Department").agg({
    "Salary": ["mean", "sum", "max"],
    "Age": ["min", "max", "mean"]
})
print(result)


#Named Aggregation (Recommended)
#This produces cleaner column names.
result = df.groupby("Department").agg(
    avg_salary=("Salary", "mean"),
    total_salary=("Salary", "sum"),
    highest_salary=("Salary", "max"),
    avg_age=("Age", "mean")
)
print(result)