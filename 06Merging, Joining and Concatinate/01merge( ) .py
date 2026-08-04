'''
pd.merge(df1, df2, on="column_name", how="type of join")
column_name = common column of both df
type of join: 
    "inner" - Only matching(common) records on both df are returned.(default)
    "outer" - Nothing disappears , fill missing values with nan.
    "left"  - Left Join (Most Used) Keep all rows from the left dataframe.
    "right" - Right Join, Keep every row from the right dataframe.
    "cross" - here we can't define on = "column_name" 
              a cross merge refers to performing a Cartesian product between two DataFrames
              Useful in recommendation systems and generating all possible combinations.(return m*n rows)
'''
import pandas as pd

df1 = pd.DataFrame({
    "Name":["Mukul", "Rahul", "Priya", "Karan", "Raj"],
    "Department": ["IT", "HR", "IT", "HR", "Finance"],
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi"],
    "Salary": [90000, 40000, 60000, 45000, 70000],
    "Experience": [2, 3, 5, 2, 8]

})

df2 = pd.DataFrame({
    "Name":["Mukul", "Karan", "Priya", "Raj","Rohit","Mukul"],
    
    "Grade":["A+", "A+", "B", "C", "A", "B"],
    "Amount":[500,700,900,1200,800,1000]
    
})

inner_merge_df = pd.merge(df1,df2, on="Name", how="inner")
print(inner_merge_df)

outer_merge_df = pd.merge(df1,df2, on="Name", how="outer")
print(outer_merge_df)

left_merge_df = pd.merge(df1,df2, on="Name", how="left")
print(left_merge_df)

right_merge_df = pd.merge(df1,df2, on="Name", how="right")
print(right_merge_df)



# Cross merge 
cross_merge = pd.merge(df1,df2, how="cross")
print(cross_merge)



# Merge on Different Column Names
'''
When you want to merge two DataFrames on columns that have different names,
 you can use the left_on and right_on parameters in pd.merge().
'''

df1 = pd.DataFrame({'emp_id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'id': [1, 2, 4], 'salary': [50000, 60000, 70000]})
result = pd.merge(df1, df2, left_on='emp_id', right_on='id', how='inner')
print(result)


#Multiple Merge Keys
'''
When you want to merge on multiple keys (columns) in pandas,
 you simply pass a list of column names to the on parameter (or to left_on and right_on if the names differ between DataFrames).
'''
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'dept': ['HR', 'IT', 'Finance'],
    'name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 3],
    'dept': ['HR', 'IT', 'Finance', 'IT'],
    'salary': [50000, 60000, 70000, 65000]
})

result = pd.merge(df1, df2, on=['id', 'dept'], how='inner')
print(result)

# Handling Duplicate Column Names
'''
Pandas handles this by automatically appending suffixes like _x and _y to distinguish them.
You can control the suffixes with the suffixes parameter:
'''
result = pd.merge(df1, df2, on='dept', how='inner', suffixes=( "_left","_right"))
print(result)

#Indicator Column
#Know where rows came from.
df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'id': [2, 3, 4], 'salary': [60000, 70000, 80000]})

result = pd.merge(df1, df2, on='id', how='outer', indicator=True)
print(result)


#Validate Merge
#Ensure expected relationships.
'''
In pandas, the validate parameter in merge() is used to check the type of join relationship between the two DataFrames.
It ensures that the merge behaves as expected and raises an error if the relationship doesn’t match.    
"one_to_one" → Each key in both DataFrames is unique.

"one_to_many" → Keys in the left DataFrame are unique, but may repeat in the right DataFrame.

"many_to_one" → Keys in the right DataFrame are unique, but may repeat in the left DataFrame.

"many_to_many" → Keys may repeat in both DataFrames (default, no validation).
'''
result = pd.merge(df1, df2, on='id', validate='one_to_one')
print(result)
# raise error if one_to_one is false, otherwise merge work well
#MergeError: Merge keys are not unique in right dataset; not a one-to-one merge