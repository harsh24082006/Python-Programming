menu = {
    'Burger': 150,
    'Pizza': 250,
    'Pasta': 200,
    'Fries': 80,
    'Coke': 50
}

print("--- Menu ---")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

total_bill = 0

while True:
    order = input("\nEnter item name to order (or type 'done' to finish): ").title()
    if order.lower() == 'done':
        break
    elif order in menu:
        total_bill += menu[order]
        print(f"Added {order} - Current Total: ₹{total_bill}")
    else:
        print("Item not on the menu. Please select a valid item.")

print(f"\n--- Final Bill ---")
print(f"Total Amount to Pay: ₹{total_bill}")
print("Thank you for ordering!")