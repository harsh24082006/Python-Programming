sports =['cricket', 'football', 'hockey', 'kabaddi', 'kho-kho']
expenses =[]

print("9. Enter your monthly expenses for playing the following sports:")

# Iterating through the sports list to collect expenses
for sport in sports:
    while True:
        try:
            cost = float(input(f"Expense for {sport.capitalize()}: Rupees"))
            expenses.append(cost)
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

print("\n--- Monthly Sports Expense Report ---")
for i in range(len(sports)):
    print(f"{sports[i].capitalize()}: Rupees {expenses[i]:.2f}")

total = sum(expenses)
print("-" * 30)
print(f"Total Expenditure: Rupees {total:.2f}")