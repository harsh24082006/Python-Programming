def check_pass_or_fail(percentage, passing_criteria=40):
    if percentage >= passing_criteria:
        return "Pass"
    else:
        return "Fail"

# User Input and Function Call
percent_score = float(input("Enter the student's percentage to check pass/fail: "))
min_pass = float(input("Enter the minimum passing percentage (e.g., 40): "))

status = check_pass_or_fail(percent_score, min_pass)
print(f"The student's status is: {status}")