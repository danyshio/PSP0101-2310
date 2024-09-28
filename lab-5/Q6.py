import math

print("A - Rectangle")
print("B - Triangle")
print("C - Circle")

shape = input("Enter shape: ")
if shape == A and shape == B:
    base = float(input("Enter height: "))
    height = float(input("Enter base: "))
    area = base * height
    print(f"Area = {area}")
elif shape == C:
    radius = float(input("Enter radius: "))
    area = radius * 2