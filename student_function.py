def total_and_percentage(marks):
    total = sum(marks)
    max_marks = len(marks) * 100 # Assuming each subject is out of 100
    percentage = (total / max_marks) * 100
    return total, round(percentage, 2)

# User Input and Function Call
num_subjects = int(input("Enter the total number of subjects: "))
student_marks = []

for i in range(num_subjects):
    mark = float(input(f"Enter marks obtained in subject {i+1} (out of 100): "))
    student_marks.append(mark)

total_marks, percent = total_and_percentage(student_marks)
print(f"\nTotal Marks: {total_marks} out of {num_subjects * 100}")
print(f"Percentage: {percent}%")