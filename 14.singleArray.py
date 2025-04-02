# 14. python program to demonstrate basic operations on single array

import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])
print("Original Array:", array)

# Basic Operations
# 1. Addition
added_array = array + 10
print("Array after addition (10):", added_array)

# 2. Multiplication
multiplied_array = array * 2
print("Array after multiplication (by 2):", multiplied_array)

# 3. Slicing
sliced_array = array[1:4]  # Get elements from index 1 to 3
print("Sliced Array (index 1 to 3):", sliced_array)

# 4. Finding the sum of the array
array_sum = np.sum(array)
print("Sum of the Array:", array_sum)

# 5. Finding the mean of the array
array_mean = np.mean(array)
print("Mean of the Array:", array_mean)


# output 

# Original Array: [1 2 3 4 5]
# Array after addition (10): [11 12 13 14 15]
# Array after multiplication (by 2): [ 2  4  6  8 10]
# Sliced Array (index 1 to 3): [2 3 4]
# Sum of the Array: 15
# Mean of the Array: 3.0