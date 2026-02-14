# Part I: Using a third variable
x, y = 10, 20
print(f"Original: x={x}, y={y}")
temp = x
x = y
y = temp
print(f"Swapped (with third var): x={x}, y={y}")

# Part ii: Without using a third variable
a, b = 30, 40
a, b = b, a
print(f"Swapped (without third var): a={a}, b={b}")