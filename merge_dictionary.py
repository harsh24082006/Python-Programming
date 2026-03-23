dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Method 1: Using the | operator (Python 3.9+)
merged_dict = dict1 | dict2

# Method 2: Using the update() method
# merged_dict = dict1.copy()
# merged_dict.update(dict2)

print("Merged Dictionary:", merged_dict)