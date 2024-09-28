#method1
drink1 = float(input("Price of drink #1: "))
drink2 = float(input("Price of drink #2: "))

if drink1 < drink2:
    total = (drink1*0.5) + drink2
    print(f"Total price = RM{total}")
else:
    total = (drink2*0.5) + drink1
    print(f"Total price = RM{total}")



#method2
drink1 = float(input("Price of drink #1: "))
drink2 = float(input("Price of drink #2: "))

if drink1 > drink2:
    total = drink2*0.5 + drink1
else:
    total = drink1*0.5 + drink2

print(f"Total price = {total}")