# 9. write a program to demonstrate working with tuples in python

def main():
    # Creating a tuple
    my_tuple = (1, 2, 3, 'apple', 'banana')
    print("Original Tuple:", my_tuple)

    # a. Adding items to a tuple (by creating a new tuple)
    new_items = ('orange', 4.5)
    my_tuple = my_tuple + new_items  # Concatenate tuples
    print("\nTuple after adding items:", my_tuple)

    # b. Finding the length of the tuple
    print("\nLength of the Tuple:", len(my_tuple))

    # c. Checking if an item exists in the tuple
    item_to_check = 'apple'
    if item_to_check in my_tuple:
        print(f"\n'{item_to_check}' is present in the tuple.")
    else:
        print(f"\n'{item_to_check}' is not present in the tuple.")

    # d. Accessing items in the tuple
    print("\nAccessing Items:")
    print("First item:", my_tuple[0])
    print("Last item:", my_tuple[-1])
    print("Items from index 1 to 3:", my_tuple[1:4])  # Slicing

if __name__ == "__main__":
    main()


# output 

# Original Tuple: (1, 2, 3, 'apple', 'banana')

# Tuple after adding items: (1, 2, 3, 'apple', 'banana', 'orange', 4.5)

# Length of the Tuple: 7

# 'apple' is present in the tuple.

# Accessing Items:
# First item: 1
# Last item: 4.5
# Items from index 1 to 3: (2, 3, 'apple')