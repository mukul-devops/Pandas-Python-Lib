'''
A Series is like a single column in Excel.
Series = Index + Values
'''
import pandas as pd
age = pd.Series([22, 35, 58, 45, 30], name='Age')  #name is optional, it is used to name the Series
print(age)                                         #output  
                                                   #         0    21
                                                   #         1    22
                                                   #         2    24
                                                   #         3    30
                                                   #         4    26
                                                   #         Name: Age, dtype: int64

#Every Series has: Index, Values, and Data Type
print(age.index)                                   #output: RangeIndex(start=0, stop=5, step=1)
print(age.values)                                  #        [21 22 24 30 26]
print(age.dtype)                                   #        int64

# Custom Index
students = pd.Series(
    [80, 95, 76],
    index=["Ram", "Shyam", "Mohan"]
)


print(students)
print(students["Shyam"])
print(students.index)                              #output: Index(['Ram', 'Shyam', 'Mohan'], dtype='object')