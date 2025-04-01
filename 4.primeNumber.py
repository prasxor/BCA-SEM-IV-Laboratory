# 4. write a python program to generate prime numbers between different intervals

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    """Generate prime numbers in the given interval."""
    return [num for num in range(start, end + 1) if is_prime(num)]

# Get user input for intervals
intervals = int(input("Enter the number of intervals: "))

for i in range(intervals):
    start = int(input(f"Enter start of interval {i+1}: "))
    end = int(input(f"Enter end of interval {i+1}: "))
    
    primes = generate_primes(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")
