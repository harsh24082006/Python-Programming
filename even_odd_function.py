def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

# User Input and Function Call
user_num = int(input("Enter an integer to check even or odd: "))
print(check_even_odd(user_num))