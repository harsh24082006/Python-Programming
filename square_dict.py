def generate_squares(n):
    # Dictionary comprehension
    return {num: num**2 for num in range(1, n + 1)}

n = int(input("Enter a number (n): "))
squares_dict = generate_squares(n)
print(f"Dictionary of squares up to {n}:", squares_dict)