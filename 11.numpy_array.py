# 11. python program to demonstrate basic array characteriestics 

import array as arr

def main():
    # Create an array of integers
    my_array = arr.array('i', [1, 2, 3, 4, 5])
    
    # Accessing elements
    print("First element:", my_array[0])
    print("Last element:", my_array[-1])
    
    # Length of the array
    print("Length of the array:", len(my_array))

if __name__ == "__main__":
    main()

# output 

# First element: 1
# Last element: 5
# Length of the array: 5