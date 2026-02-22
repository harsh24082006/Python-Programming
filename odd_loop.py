start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Odd numbers between {start} and {end}:")
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")