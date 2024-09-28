import math

print("A - Rectangle")
print("B - Triangle")
print("C - Circle")
shape = input("Enter shape: ")

if shape == "A":
    base = float(input("Enter height: "))
    height = float(input("Enter base: "))
    area = base * height
    print(f"Area = {area}")
elif shape == "B":
    base = float(input("Enter height: "))
    height = float(input("Enter base: "))
    area = base * height * 0.5
    print(f"Area = {area}")
elif shape == "C":
    radius = float(input("Enter radius: "))
    area = math.pi * radius ** 2
    print(f"Area = {area}")


#method 2

print("A - Rectangle")
print("B - Triangle")
print("C - Circle")

shape = input("Enter shape: ")

if(shape == 'A' or shape == 'B'):
    height = float(input("Enter height: "))
    base = float(input("Enter base: "))
    area = height* base
    if(shape == 'B'):
        area = 0.5*height* base
else:
    radius = float(input("Enter radius: "))
    area = math.pi*radius**2

print(f"Area = {area}")