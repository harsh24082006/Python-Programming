# No loop needed for size 10 as per manual "no need to use a loop"
# But standard logic for size 10 is:
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()