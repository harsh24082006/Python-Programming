terms = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1

print(f"Fibonacci series up to {terms} terms:")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print("\n")