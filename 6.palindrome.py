# 6. write a python program to check whether a string is palindrome or not

def is_palindrome(s):
    """Function to check if a string is a palindrome."""
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

def main():
    """Main function to take user input and check for palindrome."""
    user_input = input("Enter a string: ")
    
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()
