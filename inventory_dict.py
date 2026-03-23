inventory = {
    'Laptops': 15,
    'Smartphones': 0,
    'Tablets': 8,
    'Headphones': 0,
    'Monitors': 5
}

print("Out of stock products:")
for product, quantity in inventory.items():
    if quantity == 0:
        print(f"- {product}")