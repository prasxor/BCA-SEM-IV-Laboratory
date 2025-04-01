# 7. write a pthon program to count the number of characters present in a word

def count_characters(word):
    """Function to count the number of characters in a word."""
    return len(word)

def main():
    """Main function to take user input and display character count."""
    user_input = input("Enter a word: ")
    
    character_count = count_characters(user_input)
    
    print(f"The number of characters in '{user_input}' is: {character_count}")

if __name__ == "__main__":
    main()

