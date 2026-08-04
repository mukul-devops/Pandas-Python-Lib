'''
- .repalce() is used to change wrong values in DataFrame by passing dictionary of key value pairs.
- .replace({
     key : value,
     key : Value,..
  })

  key   - which will be changed
  value - what will be changed
'''
import pandas as pd
import numpy as np

data = {
    "ID": [1,2,3,4,5,5,6],
    "Name": ["Mukul","rahul","  Aman","Priya","Neha","neha","  mohit  "],
    "Age": [20,np.nan,19,21,23,23,25],
    "Salary": [60000,40000,42000,np.nan,48000,48000,"55000"],
    "Department": ["AI","Web","AI","Data","Web","Web","AI"],
    "City": ["Delhi NCR","Jaipur","Noida","New Delhi"," Delhi","Delhi","Mumbai"]
}

df = pd.DataFrame(data)

# Mostly use 
df["City"] = df["City"].replace({
    "Delhi NCR":"Delhi",
    "New Delhi":"Delhi"
    })

# Alternate method apply on whole array 
# df = df.replace({
#     "New Delhi":"Delhi",
#     "Delhi NCR":"Delhi",
#      60000 : 100000
# })
   

print(df)