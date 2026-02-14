s1 = float(input("Side 1: "))
s2 = float(input("Side 2: "))
s3 = float(input("Side 3: "))

if s1 == s2 == s3:
    print("Equilateral Triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")