'''
- interpolate() method is used to fill missing values (NaN) in a DataFrame by estimating them based on surrounding data points.
 It’s especially useful when working with time series or continuous data where you want smooth transitions instead of abrupt gaps.

- df.interpolate(method='polynomial')
method:
'linear' → Default, straight-line between points.

'time' → Works with datetime index.

'polynomial' → Fits polynomial curve (requires order).

'spline' → Smooth curve fitting.
'''

import pandas as pd
data = {"Time":[1,3,5,6,8],
        "Value":[10,20,None,30,50]

}

df = pd.DataFrame(data)
df["Value"] = df["Value"].interpolate(method="linear")
print(df)