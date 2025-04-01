# 1. write a python to demonstrate different number data types in python 
# Integer type
integer_num = 42
print(f"Integer: {integer_num} (Type: {type(integer_num)})")

# Float type
float_num = 3.14
print(f"Float: {float_num} (Type: {type(float_num)})")

# Complex type
complex_num = 2 + 3j
print(f"Complex: {complex_num} (Type: {type(complex_num)})")

# Demonstrating arithmetic operations with different number types
# Integer and Float
sum_result = integer_num + float_num
print(f"\nSum of Integer and Float: {sum_result} (Type: {type(sum_result)})")

# Float and Complex
complex_result = float_num + complex_num
print(f"Sum of Float and Complex: {complex_result} (Type: {type(complex_result)})")

# Integer and Complex
complex_integer_result = integer_num + complex_num
print(f"Sum of Integer and Complex: {complex_integer_result} (Type: {type(complex_integer_result)})")


# Output : 

# Integer: 42 (Type: <class 'int'>)
# Float: 3.14 (Type: <class 'float'>)
# Complex: (2+3j) (Type: <class 'complex'>)

# Sum of Integer and Float: 45.14 (Type: <class 'float'>)
# Sum of Float and Complex: (5.140000000000001+3j) (Type: <class 'complex'>)
# Sum of Integer and Complex: (44+3j) (Type: <class 'complex'>)
