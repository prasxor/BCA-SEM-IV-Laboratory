# 5. write a python program to find factorial of a number using recursion

def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Main function to take user input and display the factorial."""
    try:
        number = int(input("Enter a non-negative integer to find its factorial: "))
        result = factorial(number)
        print(f"The factorial of {number} is: {result}")
    except ValueError:
        print("Invalid input! Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()


# output 
# Enter a non-negative integer to find its factorial: 20
# The factorial of 20 is: 2432902008176640000