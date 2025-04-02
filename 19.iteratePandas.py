# 19. python code demonstrate how to iterate over rows in pandas dataframe

import pandas as pd

# Create a sample DataFrame
data = {'name': ['Mike', 'Doe', 'James'], 'age': [18, 19, 29]}
df = pd.DataFrame(data)

# Iterate over the rows using iterrows()
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['name']}, Age: {row['age']}")

# o/p 
# Index: 0, Name: Mike, Age: 18
# Index: 1, Name: Doe, Age: 19
# Index: 2, Name: James, Age: 29