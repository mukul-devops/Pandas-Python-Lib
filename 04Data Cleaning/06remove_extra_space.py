import pandas as pd
import numpy as np

data = {
    "ID": [1,2,3,4,5,5,6],
    "Name": ["Mukul","rahul","  Aman","Priya","Neha","neha","  mohit  "],
    "Age": [20,np.nan,19,21,23,23,25],
    "Salary": [60000,40000,42000,np.nan,48000,48000,"55000"],
    "Department": ["AI","Web","AI","Data","Web","Web","AI"],
    "City": ["Delhi","Jaipur","Noida","Delhi"," Delhi","Delhi","Mumbai"]
}

df = pd.DataFrame(data)

#Removing Strip Spaces
df["Name"] = df["Name"].str.strip(" ")

#Convert to Lowercase
df["Department"] = df["Department"].str.lower()

#Convert to Uppercase
df["City"] = df["City"].str.upper()

#Capitalize
df["Name"] = df["Name"].str.title()
print(df)
