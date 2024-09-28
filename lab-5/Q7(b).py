hours = float(input("Enter hours: "))

if hours <= 40:
    payment = hours * 25
    print(f"Payment = RM{payment}")
else:
    payment = (40 * 25) + (50*(hours - 40))
    print(f"Payment = RM{payment}")
