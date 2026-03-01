sports = ['cricket', 'football', 'hockey', 'kabaddi', 'kho-kho']
temperatures =[]

print("10. Enter the temperature recorded during the matches of these sports:")

for sport in sports:
    while True:
        try:
            temp = float(input(f"Temperature during {sport.capitalize()} match: "))
            temperatures.append(temp)
            break
        except ValueError:
            print("Invalid input! Please enter a numerical temperature.")

print(f"\nRecorded Temperatures: {temperatures}")
print(f"Highest match temperature: {max(temperatures)}°C (Recorded during {sports[temperatures.index(max(temperatures))]})")
print(f"Lowest match temperature: {min(temperatures)}°C (Recorded during {sports[temperatures.index(min(temperatures))]})")