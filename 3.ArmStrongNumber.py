# 3. python program to check whether a given number is armstrong number or not

def is_armstrong_number(num):
    """Function to check if a number is an Armstrong number."""
    # Convert the number to string to easily iterate over digits
    str_num = str(num)
    num_digits = len(str_num)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_num)
    
    return armstrong_sum == num

def main():
    """Main function to take user input and check for Armstrong number."""
    try:
        number = int(input("Enter a number: "))
        if is_armstrong_number(number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

# o/P 
# Enter a number: 10
# 10 is not an Armstrong number.