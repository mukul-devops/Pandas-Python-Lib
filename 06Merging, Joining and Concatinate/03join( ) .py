'''
-join()  Works mainly on indexes. Designed to combine DataFrames by index (row labels).
   Stack columns occurs
 
- left.join(right)    => df1.join(df2, how='left')
  here, how = 'left' by default


'''
import pandas as pd

employes = pd.DataFrame({
    "Name":["Amit","Rahul"]
}, index=[101,102])

salary = pd.DataFrame({
    "Salary":[50000,60000, 3445]
}, index=[101,102,103])

df = employes.join(salary)
print(df)

df = employes.join(salary, how='right')
print(df)