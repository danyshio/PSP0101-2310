hours = float(input("Enter hours: "))

payment = 0
if hours > 0:
    payment = 2.5
if hours > 1:
    payment += 1.5
if hours > 2:
    payment += 2 * (hours - 2)

print(f"Total amount = RM{payment}")