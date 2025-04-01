
# 12. python program to demonstrate array creation techniques

# Using the array module
import array as arr

# Create an array of integers
array1 = arr.array('i', [1, 2, 3, 4, 5])
print("Array using array module:", array1)

# Using NumPy
import numpy as np

# Create a 1-D NumPy array
array2 = np.array([10, 20, 30, 40, 50])
print("Array using NumPy:", array2)

# Create a range-based NumPy array
array3 = np.arange(0, 10, 2)
print("Array using np.arange:", array3)
