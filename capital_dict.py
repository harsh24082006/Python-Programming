countries_and_capitals = {
    'India': 'New Delhi',
    'USA': 'Washington D.C.',
    'France': 'Paris',
    'Japan': 'Tokyo',
    'Australia': 'Canberra'
}

# Use .title() so "india" or "INDIA" matches "India"
country = input("Enter a country name: ").title()

if country in countries_and_capitals:
    print(f"The capital of {country} is {countries_and_capitals[country]}.")
else:
    print("Sorry, country not found in our records.")