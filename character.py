char = input("Enter a character: ").lower()
if char in ('a', 'e', 'i', 'o', 'u'):
    print(f"{char} is a Vowel")
else:
    print(f"{char} is a Consonant")