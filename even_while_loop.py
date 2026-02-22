n = int(input("Enter the value of n: "))
i = 2  # The first even positive number

print(f"Even numbers up to {n}:")
while i <= n:
    print(i, end=" ")
    i += 2
print("\n")