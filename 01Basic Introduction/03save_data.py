import pandas as pd
df = pd.DataFrame({
    "Name": ["Mukul", "Karan", "Rohit"],
    "Age": [20, 19, 21],
    "Std": ["1st year", "1st year", "2nd year"]
})

print(df)

#save data as CSV, Excel, and JSON files after manipulating and cleaning the data.
df.to_csv("saved.csv", index=False)  # Save DataFrame to CSV file without index(index=False)
df.to_excel("saved.xlsx", index=False)  
df.to_json("saved.json", orient="records")  # Save DataFrame to JSON file with records orientation