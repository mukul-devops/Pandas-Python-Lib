'''
- Simple Assignment
  df["Bonus"] = 5000

- df.insert(loc,"column",value)    is a meathod used to add a column at specific location(mostly use in industry)
  loc - Index(location)
  column - Column Name
  value - List of Data(series)
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

# Adding a column at ending (5% Bonus, Total salary )
df["Bonus"] = df["Salary"] * 0.05 
df["TotalSalary"] = df["Salary"] + df["Bonus"]
print(df)

# Adding column at any location
df.insert(2, "Gender", ["Male","Male","Male","Female","Female"])
print(df)

