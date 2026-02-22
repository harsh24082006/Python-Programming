def generate_fibonacci(terms):
    fib_series = []
    a, b = 0, 1
    for _ in range(terms):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# User Input and Function Call
n_terms = int(input("Enter the number of terms for the Fibonacci series: "))
print(f"Fibonacci series: {generate_fibonacci(n_terms)}")