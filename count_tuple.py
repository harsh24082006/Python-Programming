# Tuple with repeating elements
my_tuple = (1, 5, 2, 5, 3, 5, 4)

element_to_count = 5
# Using the built-in count() method
count = my_tuple.count(element_to_count)

print(f"The element {element_to_count} occurs {count} time(s) in the tuple.")