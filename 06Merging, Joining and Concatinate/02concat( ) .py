'''
- pd.concat() is used to combine DataFrames or Series along a particular axis (rows or columns).
  Unlike merge(), which joins on keys, concat() simply stacks objects together.

  pd.concat(list of df, axis=0, ignore_index=True)
  - list of df   = [df1,df2,...]
  - axis         = By default 0 for vertical stacks(row), 1 for horizontal stacks(column)
  - ignore_index = TO rest index

  Think of concat() as gluing DataFrames together,
  while merge() is more like matching rows based on keys.
'''
import pandas as pd



df_region1 = pd.DataFrame({
    "ID":[1,2],
    "Name":["Mukul","Karan"]
})

df_region2 = pd.DataFrame({
    "ID":[3,4],
    "Name":["Rohit","Himanshu"]
})

df_concat = pd.concat([df_region1,df_region2],ignore_index=True)
print(df_concat)

df_concat = pd.concat([df_region1,df_region2], axis=1,ignore_index=True)
print(df_concat)

