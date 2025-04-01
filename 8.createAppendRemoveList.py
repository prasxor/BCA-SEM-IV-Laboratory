
# 8.write a python program to create, append and remove lists

def display_list(my_list):
    """Function to display the current list."""
    print("Current List:", my_list)

def main():
    """Main function to manage the list."""
    my_list = []  # Create an empty list
    while True:
        print("\nOptions:")
        print("1. Append an item to the list")
        print("2. Remove an item from the list")
        print("3. Display the current list")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            item = input("Enter the item to append: ")
            my_list.append(item)
            print(f"'{item}' has been appended to the list.")
        
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        
        elif choice == '3':
            display_list(my_list)
        
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid option! Please choose a valid option.")

if __name__ == "__main__":
    main()
