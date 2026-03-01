sports = ['cricket', 'football', 'hockey', 'kabaddi', 'kho-kho']
print(f"4. Initial List: {sports}")

# Using append()
new_sport = input("Enter a sport to append at the end: ")
sports.append(new_sport)
print("After append():", sports)

# Using insert()
insert_sport = input("\nEnter a sport to insert: ")
insert_pos = int(input(f"Enter the index position to insert at (0 to {len(sports)}): "))
sports.insert(insert_pos, insert_sport)
print("After insert():", sports)