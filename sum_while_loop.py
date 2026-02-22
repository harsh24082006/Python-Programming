n = int(input("Enter the value of n: "))
total_sum = 0
i = 1

while i <= n:
    total_sum += i
    i += 1

print(f"The sum of the first {n} natural numbers is: {total_sum}")