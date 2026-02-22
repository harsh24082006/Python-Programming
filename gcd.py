# Uses the Euclidean algorithm
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

a, b = num1, num2

while b != 0:
    # Continuously replace 'a' with 'b' and 'b' with the remainder
    remainder = a % b
    a = b
    b = remainder

print(f"The GCD of {num1} and {num2} is: {a}")