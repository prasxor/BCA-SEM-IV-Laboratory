
# 16.python code demonstrate to make a pandas dataframe with two-dimensional list


import pandas as pd

# Create a two-dimensional list
data = [
    [1, 'Alice', 23],
    [2, 'Bob', 30],
    [3, 'Charlie', 22]
]

# Create a DataFrame from the 2D list
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])

# Display the DataFrame
print(df)


# output 

#    ID     Name  Age
# 0   1    Alice   23
# 1   2      Bob   30
# 2   3  Charlie   22