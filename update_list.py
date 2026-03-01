sports =['cricket', 'football', 'hockey', 'kabaddi', 'kho-kho']

# Find length
print(f"2. The list contains {len(sports)} sports.")

# Update an element
print(f"Current sports: {sports}")
index = int(input(f"Enter the index to update (0 to {len(sports)-1}): "))

if 0 <= index < len(sports):
    new_sport = input("Enter the name of the new sport: ")
    sports[index] = new_sport
    print("Updated sports list:", sports)
else:
    print("Invalid index!")