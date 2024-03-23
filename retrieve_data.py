import pandas as pd

# Your code to retrieve data into a DataFrame
# For example:
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("data.csv", index=False)
