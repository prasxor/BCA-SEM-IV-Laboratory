# 15. python program to demonstrate unary operatiors in numpy (operators ke spell wrong hai, pata hai muhje, still wonder how you highlight others mistakes so easily)


import numpy as np

# Create an array
array = np.array([-1, 0, 1, 4, 9])

# Perform unary operations
square_root = np.sqrt(array[array >= 0])  # Square root of non-negative elements
absolute_values = np.abs(array)          # Absolute values of elements
negation = -array                        # Unary negation
rounded = np.round(array)                # Rounded values

# Display results
print("Original Array:", array)
print("Square Root (non-negative):", square_root)
print("Absolute Values:", absolute_values)
print("Negated Values:", negation)
print("Rounded Values:", rounded)
