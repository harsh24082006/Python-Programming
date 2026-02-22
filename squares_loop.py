n = int(input("Enter the value of n: "))

print(f"Squares of numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(f"{i}^2 = {i**2}")