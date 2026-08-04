'''
- df.rename() method is used to change labels of rows or columns in a DataFrame.
# To change column name
- df.rename(columns={
    "previous column name":"new column name "
  })

# To Rename Index 
- df.rename(index={0: "first", 1: "second"})

'''

import pandas as pd
import numpy as np

data = {
    "ID": [1,2,3,4,5,5,6],
    "Name": ["Mukul","Rahul","Aman","Priya","Neha","Neha","  Mohit  "],
    "Age": [20,np.nan,19,21,23,23,25],
    "Salary": [60000,40000,42000,np.nan,48000,48000,"55000"],
    "Department": ["AI","Web","AI","Data","Web","Web","AI"],
    "City": ["Delhi","Jaipur","Noida","Delhi","Delhi","Delhi","Mumbai"]
}

df = pd.DataFrame(data)

df = df.rename(columns={
    "Salary":"MonthlySalary",
    "Department": "Branch"
})

df= df.rename(index={
    0:"1st",
    1:"2nd",
    2:"3rd",
    3:"4th",
    4:"5th",
    5:"6th",
    6:"7th"

})

# We can also do this same task like this
df = df.rename(columns={"Salary":"MonthlySalary", "Departmnet":"Branch"},
               index={0:"1st",1:"2nd",2:"3rd",3:"4th",4:"5th",5:"6th",6:"7th"})

print(df)
