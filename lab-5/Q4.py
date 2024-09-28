first = int(input("Enter 1st number: "))
second = int(input("Enter 2nd number: "))
third = int(input("Enter 3rd number: "))

if first > second and first > third:
    print(f"{first} is the largest.")
elif second > first and second > third:
    print(f"{second} is the largest.")
else:
    print(f"{third} is the largest.")
