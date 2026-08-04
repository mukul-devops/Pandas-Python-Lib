'''

- np.where() → Creates a new array based on condition.
- In Pandas DataFrames, the main use of np.where() is to conditionally update or create columns in a fast, vectorized way.
  It’s like applying an if-else across an entire column without writing loops.

    np.where(condition, value_if_true, value_if_false)

    condition → Boolean expression (e.g., arr > 30)
    value_if_true → Returned when condition is True
    value_if_false → Returned when condition is False

'''

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Aman", "Riya", "John", "Sara", "Tom"],
    "Age": [17, 22, 35, 15, 40],
    "Salary": [25000, 50000, -70000, 18000, 90000],
    "Department": ["HR", "IT", "Sales", "IT", "HR"]
})

#Create a New Column
#Suppose we want to classify employees as Adult or Minor.
df["Status"] = np.where(df["Age"] >= 18,
                        "Adult",
                        "Minor")

print(df)


#Update an Existing Column
#Increase salaries below ₹30,000 by ₹5,000.
df["Salary"] = np.where(df["Salary"] < 30000,
                        df["Salary"] + 5000,
                        df["Salary"])

print(df)

#Replace negative salary
# df.loc[df["Salary"]<0,"Salary"] = np.nan
df["Salary"] = np.where(df["Salary"]<0,np.nan,df["Salary"])
print(df)

#Replace Missing Values
df["Salary"] = np.where(df["Salary"].isna(),df["Salary"].mean(),df["Salary"])
print(df)


#Multiple Conditions
#Suppose we want to assign salary levels:
#Salary ≥ 80,000 → High
#Salary ≥ 50,000 → Medium
#Otherwise → Low

df["Level"] = np.where(
    df["Salary"] >= 80000,
    "High",
    np.where(df["Salary"] >= 50000,
             "Medium",
             "Low")
)
print(df)


#Discount Calculation
products = pd.DataFrame({
    "Price": [500, 1200, 2500, 800]
})

products["FinalPrice"] = np.where(
    products["Price"] > 1000,
    products["Price"] * 0.9,
    products["Price"]
)

print(products)



'''
Industry Case Study

Imagine you're preparing customer data for a churn prediction model.

customers["HighValue"] = np.where(
    customers["AnnualIncome"] >= 100000,
    1,
    0
)

customers["SeniorCitizen"] = np.where(
    customers["Age"] >= 60,
    1,
    0
)

customers["EligibleLoan"] = np.where(
    (customers["CreditScore"] >= 700) &
    (customers["AnnualIncome"] >= 50000),
    "Yes",
    "No"
)
'''
