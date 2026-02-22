def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# User Input and Function Call
number = int(input("Enter a positive integer to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a Prime number.")
else:
    print(f"{number} is NOT a Prime number.")