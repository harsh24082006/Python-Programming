# Keys are Employee IDs, Values are Salaries
employees = {
    101: 50000,
    102: 60000,
    103: 45000,
    104: 75000
}

print("Original Salaries:", employees)

# Update each employee's salary
for emp_id in employees:
    employees[emp_id] += employees[emp_id] * 0.10

print("Updated Salaries (10% increase):", employees)