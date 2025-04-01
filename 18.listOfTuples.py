# 18. python code demonstrate creating a pandas dataframe using list of tuples

import pandas as pd

# Step 1: Create a list of tuples
data = [('Alice', 25, 'Engineer'),
        ('Bob', 30, 'Doctor'),
        ('Charlie', 35, 'Teacher')]

# Step 2: Define column names
columns = ['Name', 'Age', 'Profession']

# Step 3: Create the DataFrame
df = pd.DataFrame(data, columns=columns)

# Step 4: Display the DataFrame
print(df)

