def find_largest(a, b, c):
    return max(a, b, c)

# User Input and Function Call
print("--- Find the largest of three numbers ---")
n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
n3 = float(input("Enter 3rd number: "))

print(f"The largest among the three is: {find_largest(n1, n2, n3)}")