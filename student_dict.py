students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 96,
    'Eve': 88
}

# The max() function can use dict.get as the key to find the maximum value
top_student = max(students, key=students.get)

print("Student Marks:", students)
print(f"Student with the highest marks is {top_student} with {students[top_student]} marks.")