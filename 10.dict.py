
# 10. write program to demonstrate dictionaries in python

def main():
    # Creating a dictionary
    my_dict = {
        "name": "prashant kumar sinha",
        "age": 21,
        "city": "hyderabad",
        "hobbies": ["coding", "video editing", "ui/ux design", "game"]
    }
    
    print("Original Dictionary:", my_dict)

    # Accessing values
    print("\nAccessing Values:")
    print("Name:", my_dict["name"])
    print("Age:", my_dict["age"])
    
    # Adding an item
    my_dict["email"] = "alice@example.com"
    print("\nDictionary after adding email:", my_dict)

    # Updating an item
    my_dict["age"] = 25  # Update age
    print("\nDictionary after updating age:", my_dict)

    # Removing an item
    removed_hobby = my_dict.pop("hobbies")  # Remove hobbies
    print("\nDictionary after removing hobbies:", my_dict)
    print("Removed hobbies:", removed_hobby)

    # Checking if a key exists
    key_to_check = "city"
    if key_to_check in my_dict:
        print(f"\n'{key_to_check}' is present in the dictionary.")
    
    # Iterating over keys and values
    print("\nIterating over dictionary:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
