price = float(input("Enter item price: "))
tag = input("Enter tag colour: ")
member = input("Do you hace a member card? (y/n): ")

if tag == "white":
    discount = 0
elif tag == "yellow":
    discount = 25
elif tag == "red":
    discount = 50
elif tag == "blue":
    discount = 70

if member == "y":
    discount += 5

price = price - (price * discount/100)

print(f"Total discount = {discount}%")
print(f"Final price = RM{price}")