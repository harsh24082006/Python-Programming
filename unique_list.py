sports =['cricket', 'football', 'hockey', 'kabaddi', 'kho-kho']

sports.extend(['cricket', 'hockey', 'tennis']) 
print(f"5. List with duplicates: {sports}")

# Removing duplicates while preserving order
unique_sports =[]
for sport in sports:
    if sport not in unique_sports:
        unique_sports.append(sport)

print(f"List after removing duplicates: {unique_sports}")