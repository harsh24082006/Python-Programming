def calculate_average(marks):
    if len(marks) == 0:
        return 0
    average = sum(marks) / len(marks)
    return round(average, 2)

# User Input and Function Call
n = int(input("Enter the number of subjects to calculate the average: "))
marks_obtained = []

for i in range(n):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks_obtained.append(m)

avg = calculate_average(marks_obtained)
print(f"The average marks for the {n} subjects are: {avg}")