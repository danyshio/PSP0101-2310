hours = float(input("Enter hours: "))

payment = 0
if hours > 0:
    payment = 2.5
elif hours > 1:
    payment += 1.5
elif hours > 2:
    payment += 