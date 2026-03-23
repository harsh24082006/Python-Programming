# Taking a list of students where some names are repeated
students_list =["John", "Emma", "John", "Sophia", "Michael", "Emma"]

print("List of all students (with duplicates):", students_list)

# Convert to set to get unique names
unique_students = set(students_list)

print("Unique Student Names:")
for name in unique_students:
    print("-", name)