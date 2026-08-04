'''
 - groupby() is one of the most important Pandas concepts. 
  If you master it, you'll be able to solve many real-world data analysis tasks and interview questions.

 - groupby("columns") splits data into groups based on one or more columns, performs calculations on each group, and combines the results.

   This follows the Split → Apply → Combine pattern.

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


#Basic GroupBy
df.groupby("Department")
#This creates a GroupBy object. Nothing is calculated yet
#  Internal work             Finance
#                            HR
#                            IT


#Group based on one column
#Total Salary by Department
print(df.groupby("Department")["Salary"].sum())
# Internal work of        df.groupby("Department")["Salary"]                  .sum()
#                            Finance            = [70000,75000]               = 145000
#                            HR                 = [40000,45000,42000]         = 127000
#                            IT                 = [90000,60000,55000]         = 205000

#reset_index() converts it back into a normal column with index
print(df.groupby("Department")["Salary"].sum().reset_index())

#Count Employees in each department
print(df.groupby("Department")["Name"].count())

# Get Maximum Salary of each department
print(df.groupby("Department")["Salary"].max())

#Group based on multiple column
grouped = df.groupby(["Age","Name"])["Salary"].mean()
print(grouped)