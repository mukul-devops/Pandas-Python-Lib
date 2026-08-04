'''
NaN = Not a Number
None(for object data type), these represents a missing value.

df.isnull() Method - 
 Returns a DataFrame of booleans indicating whether each cell is NaN (missing value).
 True → the value is missing
 False → the value is present

df.isnull().sum() Method - 
 Counts the number of NaN values column-wise.
 Gives a quick summary of missing values in each column.
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


#Find Missing Values
print(df.isnull()) 

#Count Missing Values
#This is the command you'll use almost every day.
print(df.isnull().sum())

