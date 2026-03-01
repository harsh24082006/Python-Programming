sports =['cricket', 'football', 'hockey', 'kabaddi', 'kho-kho']

print("11. Sports Roster Search & Delete")

# Search operation
search_query = input("Enter a sport to search for: ").lower()
if search_query in sports:
    print(f"✅ Yes, '{search_query}' is found at index {sports.index(search_query)}.")
else:
    print(f"❌ No, '{search_query}' is not in the list.")

# Delete operation
delete_query = input("\nEnter a sport to delete from the list: ").lower()
if delete_query in sports:
    sports.remove(delete_query)
    print(f"'{delete_query}' has been deleted successfully.")
    print("Updated List:", sports)
else:
    print(f"Cannot delete. '{delete_query}' does not exist in the list.")