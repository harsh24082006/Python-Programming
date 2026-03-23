def main():
    # Initialize two empty sets
    set1 = {'cricket', 'football', 'tennis'} 
    set2 = {'tennis', 'badminton', 'hockey'}

    while True:
        print("\n=== SET OPERATIONS MENU ===")
        print(f"Set 1: {set1}")
        print(f"Set 2: {set2}")
        print("1. Add element to a set")
        print("2. Remove element from a set")
        print("3. Union of sets")
        print("4. Intersection of sets")
        print("5. Difference of sets (Set 1 - Set 2)")
        print("6. Symmetric Difference of sets")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            s_num = input("Which set to add to? (1 or 2): ")
            val = input("Enter the element to add: ")
            if s_num == '1':
                set1.add(val)
                print(f"'{val}' added to Set 1.")
            elif s_num == '2':
                set2.add(val)
                print(f"'{val}' added to Set 2.")
            else:
                print("Invalid set number!")

        elif choice == '2':
            s_num = input("Which set to remove from? (1 or 2): ")
            val = input("Enter the element to remove: ")
            if s_num == '1':
                set1.discard(val) # discard does not throw error if element doesn't exist
                print(f"'{val}' removed (if it existed) from Set 1.")
            elif s_num == '2':
                set2.discard(val)
                print(f"'{val}' removed (if it existed) from Set 2.")
            else:
                print("Invalid set number!")

        elif choice == '3':
            print("Union:", set1 | set2)

        elif choice == '4':
            print("Intersection:", set1 & set2)

        elif choice == '5':
            print("Difference (Set1 - Set2):", set1 - set2)

        elif choice == '6':
            print("Symmetric Difference:", set1 ^ set2)

        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid input! Please choose a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    main()