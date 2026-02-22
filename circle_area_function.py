import math

def area_of_circle(radius):
    area = math.pi * (radius ** 2)
    return round(area, 2)

# User Input and Function Call
r = float(input("Enter the radius of the circle: "))
print(f"The area of the circle with radius {r} is: {area_of_circle(r)}")