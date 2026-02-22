def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# User Input and Function Call
student_percent = float(input("Enter the student's percentage: "))
print(f"Based on {student_percent}%, the Grade is: {assign_grade(student_percent)}")