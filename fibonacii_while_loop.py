terms = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1
count = 0

print(f"Fibonacci series up to {terms} terms:")
while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print("\n")