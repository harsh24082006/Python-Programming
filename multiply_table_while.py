num = int(input("Enter a number for the multiplication table: "))
i = 1

print(f"Multiplication table of {num}:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1