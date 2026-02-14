day_num = int(input("Enter a number (1-7): "))
days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 
        5: "Friday", 6: "Saturday", 7: "Sunday"}

print(days.get(day_num, "Invalid input! Please enter 1-7."))