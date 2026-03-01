sports =['cricket', 'football', 'hockey', 'kabaddi', 'kho-kho']

while True:
    print("\n--- Sports Club Menu ---")
    print("1. View Sports")
    print("2. Add a Sport")
    print("3. Remove a Sport")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print("\nCurrent Sports List:", sports)
    elif choice == '2':
        item = input("Enter the name of the sport to add: ")
        sports.append(item.lower())
        print(f"'{item}' has been added.")
    elif choice == '3':
        item = input("Enter the name of the sport to remove: ").lower()
        if item in sports:
            sports.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print(f"'{item}' is not in the list.")
    elif choice == '4':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")