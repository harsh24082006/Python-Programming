my_string = "Beautiful Day"
vowels = "aeiouAEIOU"
count = 0

for char in my_string:
    if char in vowels:
        count += 1

print("String:", my_string)
print("Number of vowels:", count)