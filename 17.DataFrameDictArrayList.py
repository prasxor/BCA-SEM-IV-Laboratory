# 17. python code demonstrate creating DataFrame from dictionary of array and lists

import pandas as pd
import numpy as np

# Create a dictionary with NumPy arrays and lists
data = {
    'Column1': np.array([1, 2, 3, 4]),  # NumPy array
    'Column2': [10, 20, 30, 40],        # List
    'Column3': np.array([5.5, 6.5, 7.5, 8.5])  # NumPy array
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
