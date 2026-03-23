my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

key_to_check = 'age'

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary. Value: {my_dict[key_to_check]}")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")