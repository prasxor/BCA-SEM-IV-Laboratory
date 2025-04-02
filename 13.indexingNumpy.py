
# 13. python program to demonstrate indexing in numpy

import numpy as np

# 1D Array Indexing
arr1 = np.array([10, 20, 30, 40, 50])
print("1st element (1D):", arr1[0])  # Access first element
print("Last element (1D):", arr1[-1])  # Access last element

# 2D Array Indexing
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nElement at [0, 2] (2D):", arr2[0, 2])  # Access element at row=0, col=2
print("Element at [2, -1] (2D):", arr2[2, -1])  # Access last element in row=2

# Negative Indexing
print("\nSecond last element (1D):", arr1[-2])  # Access second last element

# output 

# 1st element (1D): 10
# Last element (1D): 50

# Element at [0, 2] (2D): 3
# Element at [2, -1] (2D): 9

# Second last element (1D): 40