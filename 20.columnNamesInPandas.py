# 20. python code demonstrate how to get column names in pandas dataframe

import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Profession': ['Engineer', 'Doctor', 'Teacher']}
df = pd.DataFrame(data)

# Method 1: Using the .columns attribute
print("Column names using .columns:")
print(df.columns)

# Method 2: Converting column names to a list
column_names_list = df.columns.tolist()
print("\nColumn names as a list:")
print(column_names_list)

# Method 3: Using the keys() method (equivalent to .columns)
print("\nColumn names using keys():")
print(df.keys())


# o/p 

# Column names using .columns:
# Index(['Name', 'Age', 'Profession'], dtype='object')

# Column names as a list:
# ['Name', 'Age', 'Profession']

# Column names using keys():
# Index(['Name', 'Age', 'Profession'], dtype='object')