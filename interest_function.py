def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

# User Input and Function Call
p = float(input("Enter the Principal amount: "))
r = float(input("Enter the Rate of interest (%): "))
t = float(input("Enter the Time period (in years): "))

interest = calculate_simple_interest(p, r, t)
print(f"Simple Interest is: {interest}")